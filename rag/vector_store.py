import json
import chromadb
from sentence_transformers import SentenceTransformer


# =========================================================
# FILE PATHS
# =========================================================

PRODUCT_FILE = "data/products.json"
CHROMA_PATH = "./chroma_db"


# =========================================================
# PRODUCT RAG CLASS
# =========================================================

class ProductRAG:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.client = chromadb.PersistentClient(
            path=CHROMA_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name="electronics"
        )

        self.load_products()


    # =====================================================
    # LOAD PRODUCTS
    # =====================================================

    def load_products(self):

        with open(
            PRODUCT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            products = json.load(file)


        print(f"Products found: {len(products)}")


        # Prevent duplicate products
        if self.collection.count() > 0:

            print(
                f"ChromaDB already contains "
                f"{self.collection.count()} products."
            )

            return


        documents = []
        ids = []
        metadatas = []


        # =================================================
        # CREATE DOCUMENTS
        # =================================================

        for product in products:

            text = f"""
Product: {product['name']}
Category: {product['category']}
Brand: {product['brand']}
Price: ₹{product['price']}
Processor: {product['processor']}
RAM: {product['ram']}
Storage: {product['storage']}
Display: {product['display']}
Battery: {product['battery']}
Camera: {product['camera']}
Operating System: {product['os']}
Gaming: {product['gaming']}
Performance: {product['performance']}
Battery Rating: {product['battery_rating']}
"""


            documents.append(text)

            ids.append(product["id"])


            metadatas.append({
                "name": product["name"],
                "category": product["category"],
                "brand": product["brand"]
            })


        # =================================================
        # CREATE EMBEDDINGS
        # =================================================

        print("Creating embeddings...")


        embeddings = self.model.encode(
            documents,
            show_progress_bar=True
        ).tolist()


        # =================================================
        # STORE IN CHROMADB
        # =================================================

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )


        print(
            f"{len(products)} products added to ChromaDB."
        )


    # =====================================================
    # SEARCH PRODUCTS
    # =====================================================

    def search(
        self,
        query,
        n_results=5
    ):

        query_embedding = self.model.encode(
            [query]
        ).tolist()


        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )


        return results["documents"][0]


# =========================================================
# TEST RAG
# =========================================================

if __name__ == "__main__":

    rag = ProductRAG()


    print("\nTesting RAG Search...\n")


    results = rag.search(
        "best laptop for coding and gaming",
        n_results=3
    )


    for result in results:

        print(result)

        print("-" * 60)