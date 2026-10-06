import streamlit as st
import ollama
import json
from datetime import datetime

from rag.vector_store import ProductRAG


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ElectroCompare AI",
    page_icon="⚡",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    font-size: 18px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD PRODUCTS
# =========================================================

@st.cache_data
def load_products():

    with open(
        "data/products.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


products = load_products()


# =========================================================
# LOAD RAG
# =========================================================

@st.cache_resource
def load_rag():

    return ProductRAG()


rag = load_rag()


# =========================================================
# CATEGORY NAMES
# =========================================================

category_names = {
    "Smartphone": "📱 Smartphones",
    "Laptop": "💻 Laptops",
    "Headphones": "🎧 Earbuds / Headphones",
    "Smartwatch": "⌚ Smartwatches",
    "TV": "📺 TVs",
    "Camera": "📷 Cameras",
    "Gaming": "🎮 Gaming"
}


# =========================================================
# SESSION STATE
# =========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_chat" not in st.session_state:
    st.session_state.current_chat = []

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None


# =========================================================
# NEW CHAT
# =========================================================

def new_chat():

    if st.session_state.current_chat:

        first_message = next(
            (
                msg["content"]
                for msg in st.session_state.current_chat
                if msg["role"] == "user"
            ),
            "New Conversation"
        )

        chat = {
            "id": datetime.now().strftime(
                "%Y%m%d%H%M%S%f"
            ),
            "title": first_message[:35],
            "messages": st.session_state.current_chat.copy()
        }

        st.session_state.chat_history.insert(
            0,
            chat
        )

    st.session_state.current_chat = []
    st.session_state.current_chat_id = None


# =========================================================
# LOAD CHAT
# =========================================================

def load_chat(chat):

    st.session_state.current_chat = chat["messages"].copy()
    st.session_state.current_chat_id = chat["id"]


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("⚡ ElectroCompare AI")

    # -----------------------------------------------------
    # NEW CHAT
    # -----------------------------------------------------

    if st.button(
        "🆕 New Chat",
        use_container_width=True
    ):

        new_chat()
        st.rerun()


    st.divider()


    # -----------------------------------------------------
    # CHAT HISTORY
    # -----------------------------------------------------

    st.subheader("💬 Chat History")

    if st.session_state.chat_history:

        for chat in st.session_state.chat_history:

            if st.button(
                f"💬 {chat['title']}",
                key=f"chat_{chat['id']}",
                use_container_width=True
            ):

                load_chat(chat)
                st.rerun()

    else:

        st.caption("No previous chats yet.")


    st.divider()


    # -----------------------------------------------------
    # ELECTRONICS
    # -----------------------------------------------------

    st.subheader("🔌 Electronics")

    categories = [
        "Smartphone",
        "Laptop",
        "Headphones",
        "Smartwatch",
        "TV",
        "Camera",
        "Gaming"
    ]

    selected_category = st.radio(
        "Choose a category:",
        categories,
        format_func=lambda x: category_names[x]
    )


    st.divider()


    # -----------------------------------------------------
    # PRODUCTS
    # -----------------------------------------------------

    st.subheader(
        category_names[selected_category]
    )

    category_products = [
        product["name"]
        for product in products
        if product["category"] == selected_category
    ]

    selected_products = st.multiselect(
        "Select up to 3 products:",
        category_products,
        max_selections=3,
        placeholder="Choose products"
    )


    st.divider()


    # -----------------------------------------------------
    # SELECTED PRODUCTS
    # -----------------------------------------------------

    st.subheader("✅ Selected")

    if selected_products:

        for product in selected_products:
            st.write(f"• {product}")

    else:

        st.caption("No products selected")


# =========================================================
# MAIN PAGE
# =========================================================

st.markdown(
    '<div class="main-title">'
    '⚡ ElectroCompare AI'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Electronics Comparison Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# DISPLAY CHAT
# =========================================================

for message in st.session_state.current_chat:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

user_input = st.chat_input(
    "Ask me to compare products..."
)


# =========================================================
# PROCESS CHAT
# =========================================================

if user_input:

    # -----------------------------------------------------
    # USER MESSAGE
    # -----------------------------------------------------

    st.session_state.current_chat.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):

        st.markdown(user_input)


    # -----------------------------------------------------
    # SEARCH QUERY
    # -----------------------------------------------------

    search_query = user_input

    if selected_products:

        search_query += (
            "\nSelected products: "
            + ", ".join(selected_products)
        )


    # -----------------------------------------------------
    # RAG SEARCH
    # -----------------------------------------------------

    with st.spinner(
        "🔎 Searching product database..."
    ):

        retrieved_products = rag.search(
            search_query,
            n_results=8
        )

    context = "\n\n".join(
        retrieved_products
    )


    # -----------------------------------------------------
    # AI PROMPT
    # -----------------------------------------------------

    prompt = f"""
You are ElectroCompare AI.

You are an AI electronics product comparison assistant.

USER QUESTION:
{user_input}

SELECTED CATEGORY:
{category_names[selected_category]}

SELECTED PRODUCTS:
{", ".join(selected_products)
if selected_products else "None"}

PRODUCT DATABASE:
{context}


RULES:

1. Understand the user's requirements.
2. Compare the products clearly.
3. Give priority to selected products.
4. Use only information from the database.
5. Do not invent specifications.
6. Consider:
   - Price
   - Performance
   - Battery
   - Display
   - Camera
   - RAM
   - Storage
   - Gaming
   - Value for money
7. Recommend the best product for the user's requirement.
8. If information is unavailable, say so.


ANSWER FORMAT:

🏆 BEST CHOICE

Give the best product and explain why.


📊 COMPARISON

Compare the products.


⚡ PERFORMANCE

Explain performance.


🔋 BATTERY

Explain battery.


📷 CAMERA / DISPLAY

Explain camera or display when relevant.


💰 VALUE FOR MONEY

Explain price and value.


👍 PROS

- Advantage
- Advantage
- Advantage


👎 CONS

- Disadvantage
- Disadvantage


🎯 FINAL VERDICT

Give a short and clear recommendation.
"""


    # -----------------------------------------------------
    # OLLAMA
    # -----------------------------------------------------

    with st.spinner(
        "🤖 ElectroCompare AI is thinking..."
    ):

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


    answer = response["message"]["content"]


    # -----------------------------------------------------
    # DISPLAY RESPONSE
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        st.markdown(answer)


    # -----------------------------------------------------
    # SAVE RESPONSE
    # -----------------------------------------------------

    st.session_state.current_chat.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()