import json
import os


# =========================================================
# 50 PRODUCTS - EACH CATEGORY
# =========================================================

smartphones = [
    "Apple iPhone 16",
    "Apple iPhone 16 Plus",
    "Apple iPhone 16 Pro",
    "Apple iPhone 16 Pro Max",
    "Apple iPhone 15",
    "Apple iPhone 15 Plus",
    "Apple iPhone 15 Pro",
    "Apple iPhone 15 Pro Max",
    "Samsung Galaxy S25",
    "Samsung Galaxy S25 Plus",
    "Samsung Galaxy S25 Ultra",
    "Samsung Galaxy S24",
    "Samsung Galaxy S24 Plus",
    "Samsung Galaxy S24 Ultra",
    "Samsung Galaxy S23",
    "Samsung Galaxy S23 Ultra",
    "OnePlus 13",
    "OnePlus 13R",
    "OnePlus 12",
    "OnePlus 12R",
    "OnePlus Nord 4",
    "OnePlus Nord CE4",
    "Google Pixel 9",
    "Google Pixel 9 Pro",
    "Google Pixel 9 Pro XL",
    "Google Pixel 8",
    "Google Pixel 8 Pro",
    "Xiaomi 14",
    "Xiaomi 14 Ultra",
    "Xiaomi 14 Civi",
    "Nothing Phone (2)",
    "Nothing Phone (2a)",
    "Nothing Phone (3a)",
    "Nothing Phone (3a) Pro",
    "Motorola Edge 50 Pro",
    "Motorola Edge 50 Ultra",
    "Motorola Edge 50 Fusion",
    "Vivo X100",
    "Vivo X100 Pro",
    "Vivo V40",
    "Vivo V40 Pro",
    "Realme GT 6",
    "Realme GT 6T",
    "Realme 13 Pro+",
    "Poco F6",
    "Poco X6 Pro",
    "iQOO 12",
    "iQOO Neo 9 Pro",
    "Oppo Find X8",
    "Oppo Reno 12 Pro"
]


laptops = [
    "Apple MacBook Air M3",
    "Apple MacBook Air M2",
    "Apple MacBook Pro M3",
    "Apple MacBook Pro M3 Pro",
    "Apple MacBook Pro M3 Max",
    "Dell Inspiron 14",
    "Dell Inspiron 15",
    "Dell Inspiron 16",
    "Dell XPS 13",
    "Dell XPS 14",
    "Dell XPS 16",
    "Dell G15 Gaming",
    "Dell G16 Gaming",
    "HP Pavilion 14",
    "HP Pavilion 15",
    "HP Pavilion Plus 14",
    "HP Envy 14",
    "HP Envy 16",
    "HP Spectre x360 14",
    "HP Spectre x360 16",
    "HP Victus 15",
    "HP Victus 16",
    "HP Omen 16",
    "Lenovo IdeaPad Slim 3",
    "Lenovo IdeaPad Slim 5",
    "Lenovo IdeaPad Pro 5",
    "Lenovo Yoga Slim 6",
    "Lenovo Yoga 7",
    "Lenovo Yoga Pro 7",
    "Lenovo ThinkPad E14",
    "Lenovo ThinkPad E16",
    "Lenovo ThinkPad T14",
    "Lenovo LOQ 15",
    "Lenovo LOQ 16",
    "Lenovo Legion 5",
    "Lenovo Legion 7",
    "ASUS Vivobook 14",
    "ASUS Vivobook 15",
    "ASUS Vivobook S15",
    "ASUS Zenbook 14",
    "ASUS Zenbook 16",
    "ASUS ROG Strix G16",
    "ASUS ROG Strix G18",
    "ASUS TUF Gaming F15",
    "ASUS TUF Gaming A15",
    "Acer Aspire 5",
    "Acer Swift Go 14",
    "Acer Swift Go 16",
    "Acer Nitro V 15",
    "Acer Predator Helios Neo 16"
]


headphones = [
    "Sony WH-1000XM5",
    "Sony WH-1000XM4",
    "Sony WH-CH720N",
    "Sony WH-CH520",
    "Sony WF-1000XM5",
    "Sony WF-1000XM4",
    "Bose QuietComfort Ultra",
    "Bose QuietComfort",
    "Bose QuietComfort Earbuds II",
    "Bose Ultra Open Earbuds",
    "Apple AirPods Pro 2",
    "Apple AirPods 4",
    "Apple AirPods Max",
    "Samsung Galaxy Buds3 Pro",
    "Samsung Galaxy Buds3",
    "Samsung Galaxy Buds2 Pro",
    "OnePlus Buds Pro 3",
    "OnePlus Buds 3",
    "OnePlus Nord Buds 3 Pro",
    "Nothing Ear",
    "Nothing Ear (a)",
    "JBL Live 770NC",
    "JBL Live 670NC",
    "JBL Tune 770NC",
    "JBL Tune 760NC",
    "JBL Tour One M2",
    "Sennheiser Momentum 4",
    "Sennheiser Momentum True Wireless 4",
    "Sennheiser Accentum Plus",
    "Sennheiser HD 450BT",
    "Sennheiser HD 599",
    "Audio-Technica ATH-M50x",
    "Audio-Technica ATH-M40x",
    "Audio-Technica ATH-SR50BT",
    "Beats Studio Pro",
    "Beats Solo 4",
    "Beats Fit Pro",
    "Beats Studio Buds+",
    "Skullcandy Crusher ANC 2",
    "Skullcandy Hesh ANC",
    "Skullcandy Dime 3",
    "Realme Buds Air 6 Pro",
    "Realme Buds Air 6",
    "Realme Buds T310",
    "Oppo Enco Air 4 Pro",
    "Oppo Enco Buds2",
    "Jabra Elite 10",
    "Jabra Elite 8 Active",
    "Jabra Elite 4",
    "Anker Soundcore Space Q45"
]


smartwatches = [
    "Apple Watch Series 10",
    "Apple Watch Series 9",
    "Apple Watch Ultra 2",
    "Samsung Galaxy Watch7",
    "Samsung Galaxy Watch Ultra",
    "Samsung Galaxy Watch6",
    "Google Pixel Watch 3",
    "Google Pixel Watch 2",
    "OnePlus Watch 2",
    "OnePlus Watch 2R",
    "OnePlus Watch",
    "Xiaomi Watch 2",
    "Xiaomi Watch S3",
    "Xiaomi Watch S4",
    "Redmi Watch 5",
    "Redmi Watch 4",
    "Amazfit GTR 4",
    "Amazfit GTR Mini",
    "Amazfit Balance",
    "Amazfit Active",
    "Amazfit Active 2",
    "Garmin Venu 3",
    "Garmin Vivoactive 5",
    "Garmin Forerunner 165",
    "Garmin Forerunner 265",
    "Garmin Instinct 2",
    "Huawei Watch GT 5",
    "Huawei Watch GT 4",
    "Huawei Watch Fit 3",
    "Huawei Watch 4",
    "Noise ColorFit Pro 6",
    "NoiseFit Voyage",
    "NoiseFit Vortex Plus",
    "NoiseFit Halo",
    "boAt Lunar Pro",
    "boAt Ultima Chronos",
    "boAt Storm Call",
    "boAt Wave Sigma",
    "Fire-Boltt Phoenix",
    "Fire-Boltt Ninja Call Pro",
    "Fire-Boltt Rise",
    "Fastrack Limitless FS1",
    "Fastrack Optimus",
    "CMF Watch Pro 2",
    "CMF Watch Pro",
    "Titan Smart 3",
    "Fitbit Versa 4",
    "Fitbit Sense 2",
    "Fitbit Charge 6",
    "Fossil Gen 6"
]


tvs = [
    "Samsung 55-inch QLED 4K",
    "Samsung 65-inch QLED 4K",
    "Samsung 75-inch QLED 4K",
    "Samsung 55-inch OLED",
    "Samsung 65-inch OLED",
    "Samsung 55-inch Crystal 4K",
    "Samsung 65-inch Crystal 4K",
    "LG 55-inch OLED C4",
    "LG 65-inch OLED C4",
    "LG 77-inch OLED C4",
    "LG 55-inch OLED B4",
    "LG 65-inch OLED B4",
    "LG 55-inch QNED",
    "LG 65-inch QNED",
    "Sony 55-inch Bravia 3",
    "Sony 65-inch Bravia 3",
    "Sony 55-inch Bravia 7",
    "Sony 65-inch Bravia 7",
    "Sony 55-inch Bravia 8",
    "Sony 65-inch Bravia 8",
    "Sony 55-inch X90L",
    "Sony 65-inch X90L",
    "OnePlus 43-inch 4K TV",
    "OnePlus 50-inch 4K TV",
    "OnePlus 55-inch 4K TV",
    "OnePlus 65-inch 4K TV",
    "TCL 43-inch QLED",
    "TCL 50-inch QLED",
    "TCL 55-inch QLED",
    "TCL 65-inch QLED",
    "TCL 75-inch QLED",
    "Hisense 43-inch 4K TV",
    "Hisense 50-inch 4K TV",
    "Hisense 55-inch 4K TV",
    "Hisense 65-inch 4K TV",
    "Xiaomi 43-inch X Series",
    "Xiaomi 50-inch X Series",
    "Xiaomi 55-inch X Series",
    "Xiaomi 65-inch X Series",
    "Redmi 43-inch Smart TV",
    "Redmi 50-inch Smart TV",
    "Redmi 55-inch Smart TV",
    "Acer 43-inch Advanced I Series",
    "Acer 50-inch Advanced I Series",
    "Acer 55-inch Advanced I Series",
    "Vu 43-inch Masterpiece",
    "Vu 55-inch Masterpiece",
    "Vu 65-inch Masterpiece",
    "Motorola 55-inch EnvisionX"
]


cameras = [
    "Sony Alpha A7 IV",
    "Sony Alpha A7C II",
    "Sony Alpha A7R V",
    "Sony Alpha A6700",
    "Sony Alpha A6400",
    "Sony ZV-E10 II",
    "Sony ZV-E10",
    "Canon EOS R5",
    "Canon EOS R6 Mark II",
    "Canon EOS R8",
    "Canon EOS R7",
    "Canon EOS R10",
    "Canon EOS R50",
    "Canon EOS R100",
    "Canon EOS 90D",
    "Canon EOS 850D",
    "Nikon Z8",
    "Nikon Z6 III",
    "Nikon Zf",
    "Nikon Z7 II",
    "Nikon Z6 II",
    "Nikon Z50 II",
    "Nikon Z50",
    "Nikon D850",
    "Nikon D780",
    "Fujifilm X-T5",
    "Fujifilm X-T50",
    "Fujifilm X-S20",
    "Fujifilm X100VI",
    "Fujifilm X-H2",
    "Fujifilm X-H2S",
    "Fujifilm X-T30 II",
    "Panasonic Lumix S5 II",
    "Panasonic Lumix S5 IIX",
    "Panasonic Lumix GH6",
    "Panasonic Lumix G9 II",
    "GoPro HERO13 Black",
    "GoPro HERO12 Black",
    "GoPro MAX",
    "DJI Osmo Action 5 Pro",
    "DJI Osmo Action 4",
    "DJI Pocket 3",
    "DJI Action 2",
    "Insta360 X4",
    "Insta360 X3",
    "Insta360 Ace Pro",
    "Insta360 Ace Pro 2",
    "OM System OM-1 Mark II",
    "OM System OM-5",
    "Pentax K-3 Mark III"
]


gaming = [
    "PlayStation 5 Slim",
    "PlayStation 5 Pro",
    "Xbox Series X",
    "Xbox Series S",
    "Nintendo Switch OLED",
    "Nintendo Switch Lite",
    "Nintendo Switch",
    "Steam Deck OLED",
    "Steam Deck LCD",
    "ASUS ROG Ally",
    "ASUS ROG Ally X",
    "Lenovo Legion Go",
    "MSI Claw",
    "Acer Nitro V Gaming",
    "ASUS ROG Strix G16",
    "ASUS ROG Strix G18",
    "ASUS TUF Gaming A15",
    "ASUS TUF Gaming F15",
    "Lenovo Legion 5",
    "Lenovo Legion 7",
    "Lenovo LOQ Gaming",
    "HP Victus Gaming",
    "HP Omen Gaming",
    "Dell G15 Gaming",
    "Dell G16 Gaming",
    "Alienware m16",
    "Alienware x16",
    "MSI Katana 15",
    "MSI Cyborg 15",
    "MSI Raider GE68",
    "MSI Vector 16",
    "Acer Nitro 5",
    "Acer Nitro V",
    "Acer Predator Helios Neo 16",
    "Acer Predator Helios 18",
    "Razer Blade 14",
    "Razer Blade 15",
    "Razer Blade 16",
    "Razer Blade 18",
    "Logitech G Cloud",
    "Logitech G Pro X 2",
    "Logitech G733",
    "Logitech G502 X",
    "Razer BlackShark V2 Pro",
    "Razer DeathAdder V3",
    "SteelSeries Arctis Nova 7",
    "SteelSeries Arctis Nova Pro",
    "Xbox Wireless Controller",
    "PlayStation DualSense Controller",
    "Nintendo Pro Controller"
]


# =========================================================
# CATEGORY CONFIGURATION
# =========================================================

categories = {
    "Smartphone": smartphones,
    "Laptop": laptops,
    "Headphones": headphones,
    "Smartwatch": smartwatches,
    "TV": tvs,
    "Camera": cameras,
    "Gaming": gaming
}


# =========================================================
# DEMO PRODUCT DATA GENERATOR
# =========================================================

def create_product(product_id, name, category):

    brand = name.split()[0]

    if category == "Smartphone":
        return {
            "id": product_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": 39999,
            "processor": "Modern Octa-Core Processor",
            "ram": "8GB",
            "storage": "256GB",
            "display": "6.5-inch AMOLED 120Hz",
            "battery": "5000 mAh",
            "camera": "50MP Dual Camera",
            "os": "Android",
            "gaming": "Good",
            "performance": "Very Good",
            "battery_rating": "Very Good"
        }

    elif category == "Laptop":
        return {
            "id": product_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": 74999,
            "processor": "Intel Core / AMD Ryzen / Apple Silicon",
            "ram": "16GB",
            "storage": "512GB SSD",
            "display": "14-inch Full HD Display",
            "battery": "Up to 10 hours",
            "camera": "1080p Webcam",
            "os": "Windows / macOS",
            "gaming": "Good",
            "performance": "Very Good",
            "battery_rating": "Very Good"
        }

    elif category == "Headphones":
        return {
            "id": product_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": 14999,
            "processor": "Integrated Audio Processor",
            "ram": "N/A",
            "storage": "N/A",
            "display": "N/A",
            "battery": "Up to 30 hours",
            "camera": "N/A",
            "os": "N/A",
            "gaming": "Good",
            "performance": "Very Good",
            "battery_rating": "Excellent"
        }

    elif category == "Smartwatch":
        return {
            "id": product_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": 9999,
            "processor": "Smartwatch Processor",
            "ram": "2GB",
            "storage": "32GB",
            "display": "AMOLED Display",
            "battery": "Up to 7 days",
            "camera": "N/A",
            "os": "Wearable OS",
            "gaming": "Basic",
            "performance": "Very Good",
            "battery_rating": "Excellent"
        }

    elif category == "TV":
        return {
            "id": product_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": 54999,
            "processor": "Smart TV Processor",
            "ram": "2GB",
            "storage": "16GB",
            "display": "4K UHD",
            "battery": "N/A",
            "camera": "N/A",
            "os": "Smart TV OS",
            "gaming": "Very Good",
            "performance": "Very Good",
            "battery_rating": "N/A"
        }

    elif category == "Camera":
        return {
            "id": product_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": 99999,
            "processor": "Advanced Image Processor",
            "ram": "N/A",
            "storage": "SD Card",
            "display": "3-inch LCD",
            "battery": "Up to 600 shots",
            "camera": "24MP+ Sensor",
            "os": "Camera Firmware",
            "gaming": "N/A",
            "performance": "Excellent",
            "battery_rating": "Very Good"
        }

    else:
        return {
            "id": product_id,
            "name": name,
            "category": category,
            "brand": brand,
            "price": 69999,
            "processor": "Gaming Processor",
            "ram": "16GB",
            "storage": "512GB SSD",
            "display": "16-inch 165Hz Display",
            "battery": "Up to 8 hours",
            "camera": "1080p Webcam",
            "os": "Windows",
            "gaming": "Excellent",
            "performance": "Excellent",
            "battery_rating": "Good"
        }


# =========================================================
# CREATE 350 PRODUCTS
# =========================================================

products = []

counter = 1

for category, product_list in categories.items():

    for name in product_list:

        product = create_product(
            product_id=f"P{counter:03d}",
            name=name,
            category=category
        )

        products.append(product)
        counter += 1


# =========================================================
# SAVE JSON
# =========================================================

os.makedirs("data", exist_ok=True)

with open(
    "data/products.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        products,
        file,
        indent=4,
        ensure_ascii=False
    )


# =========================================================
# RESULT
# =========================================================

print("=" * 50)
print("ElectroCompare AI Dataset Created")
print("=" * 50)

for category, product_list in categories.items():
    print(f"{category}: {len(product_list)} products")

print("-" * 50)
print(f"TOTAL PRODUCTS: {len(products)}")
print("-" * 50)

print("Saved to: data/products.json")