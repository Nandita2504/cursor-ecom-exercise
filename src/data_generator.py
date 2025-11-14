import csv
import random
from datetime import date, timedelta
from pathlib import Path


def main() -> None:
    random.seed(42)
    root = Path(__file__).resolve().parent

    categories = [
        "Electronics",
        "Home",
        "Outdoors",
        "Beauty",
        "Toys",
        "Clothing",
        "Kitchen",
        "Books",
        "Fitness",
        "Garden",
    ]

    product_names = [
        "Bluetooth Speaker",
        "Ceramic Vase",
        "Camping Lantern",
        "Face Serum",
        "Puzzle Kit",
        "Running Shoes",
        "Chef Knife",
        "Thriller Novel",
        "Yoga Mat",
        "Garden Hose",
        "Wireless Mouse",
        "Wall Clock",
        "Hammock",
        "Hair Dryer",
        "Board Game",
        "Denim Jacket",
        "Espresso Maker",
        "Cookbook",
        "Resistance Bands",
        "Planter Set",
        "Noise-Canceling Headphones",
        "Floor Lamp",
        "Travel Backpack",
        "Lipstick Duo",
        "RC Car",
        "Winter Coat",
        "Air Fryer",
        "Historical Fiction",
        "Foam Roller",
        "Pruning Shears",
        "Smartwatch",
        "Throw Blanket",
        "Portable Grill",
        "Moisturizer",
        "STEM Kit",
        "Hiking Boots",
        "Blender",
        "Mystery Series",
        "Jump Rope",
        "Seed Starter",
        "Gaming Keyboard",
        "Table Runner",
        "Kayak Paddle",
        "Hair Mask",
        "Drone",
        "Rain Jacket",
        "Slow Cooker",
        "Fantasy Saga",
        "Kettlebell",
        "Outdoor Lights",
    ]

    products = []
    for i in range(50):
        product_id = 1001 + i
        name = product_names[i]
        category = categories[i % len(categories)]
        price = round(random.uniform(12, 250), 2)
        sku = f"SKU-{product_id}"
        in_stock = random.choice(["True", "True", "True", "False"])
        products.append(
            {
                "product_id": product_id,
                "sku": sku,
                "name": name,
                "category": category,
                "price": f"{price:.2f}",
                "in_stock": in_stock,
            }
        )

    first_names = [
        "Ava",
        "Liam",
        "Sophia",
        "Noah",
        "Isabella",
        "Mason",
        "Mia",
        "Ethan",
        "Charlotte",
        "Logan",
        "Amelia",
        "Lucas",
        "Harper",
        "Jackson",
        "Evelyn",
        "Aiden",
        "Abigail",
        "Elijah",
        "Emily",
        "Oliver",
        "Aria",
        "Carter",
        "Scarlett",
        "James",
        "Victoria",
        "Wyatt",
        "Grace",
        "Sebastian",
        "Chloe",
        "Henry",
        "Layla",
        "Owen",
        "Zoe",
        "Gabriel",
        "Penelope",
        "Caleb",
        "Lily",
        "Jayden",
        "Hannah",
        "Julian",
        "Nora",
        "Levi",
        "Avery",
        "Isaac",
        "Ella",
        "Mateo",
        "Aurora",
        "David",
        "Savannah",
        "Joseph",
    ]

    last_names = [
        "Johnson",
        "Smith",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Gonzalez",
        "Wilson",
        "Anderson",
        "Thomas",
        "Taylor",
        "Moore",
        "Jackson",
        "Martin",
        "Lee",
        "Perez",
        "Thompson",
        "White",
        "Harris",
        "Sanchez",
        "Clark",
        "Ramirez",
        "Lewis",
        "Robinson",
        "Walker",
        "Young",
        "Allen",
        "King",
        "Wright",
        "Scott",
        "Torres",
        "Nguyen",
        "Hill",
        "Flores",
        "Green",
        "Adams",
        "Nelson",
        "Baker",
        "Hall",
        "Rivera",
        "Campbell",
        "Mitchell",
        "Carter",
        "Roberts",
    ]

    cities = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "Seattle",
        "Austin",
        "Boston",
        "Denver",
        "Miami",
    ]

    countries = ["USA", "Canada", "UK", "Germany", "Australia"]

    customers = []
    base_signup = date(2023, 1, 5)
    for i in range(50):
        customer_id = 2001 + i
        first = first_names[i]
        last = last_names[i]
        email = f"{first.lower()}.{last.lower()}@example.com"
        signup_date = base_signup + timedelta(days=i * 3)
        city = cities[i % len(cities)]
        country = countries[i % len(countries)]
        customers.append(
            {
                "customer_id": customer_id,
                "first_name": first,
                "last_name": last,
                "email": email,
                "signup_date": signup_date.isoformat(),
                "city": city,
                "country": country,
            }
        )

    orders = []
    order_items = []
    reviews = []
    base_order_date = date(2024, 2, 1)
    statuses = ["completed", "completed", "completed", "pending", "cancelled", "refunded"]
    product_price_map = {int(p["product_id"]): float(p["price"]) for p in products}

    for i in range(50):
        order_id = 3001 + i
        customer = customers[i]
        product = products[i]
        quantity = random.randint(1, 4)
        unit_price = product_price_map[int(product["product_id"])]
        line_total = round(quantity * unit_price, 2)
        order_date = base_order_date + timedelta(days=i)
        status = statuses[i % len(statuses)]

        orders.append(
            {
                "order_id": order_id,
                "customer_id": customer["customer_id"],
                "order_date": order_date.isoformat(),
                "total_amount": f"{line_total:.2f}",
                "status": status,
            }
        )

        order_items.append(
            {
                "order_item_id": 4001 + i,
                "order_id": order_id,
                "product_id": product["product_id"],
                "quantity": quantity,
                "unit_price": f"{unit_price:.2f}",
                "line_total": f"{line_total:.2f}",
            }
        )

        review_date = order_date + timedelta(days=7)
        rating = random.randint(3, 5)
        review_text = f"Loved the {product['name'].lower()}!"
        reviews.append(
            {
                "review_id": 5001 + i,
                "product_id": product["product_id"],
                "customer_id": customer["customer_id"],
                "review_date": review_date.isoformat(),
                "rating": rating,
                "review_text": review_text,
            }
        )

    files = [
        (
            "products.csv",
            ["product_id", "sku", "name", "category", "price", "in_stock"],
            products,
        ),
        (
            "customers.csv",
            [
                "customer_id",
                "first_name",
                "last_name",
                "email",
                "signup_date",
                "city",
                "country",
            ],
            customers,
        ),
        (
            "orders.csv",
            ["order_id", "customer_id", "order_date", "total_amount", "status"],
            orders,
        ),
        (
            "order_items.csv",
            [
                "order_item_id",
                "order_id",
                "product_id",
                "quantity",
                "unit_price",
                "line_total",
            ],
            order_items,
        ),
        (
            "reviews.csv",
            [
                "review_id",
                "product_id",
                "customer_id",
                "review_date",
                "rating",
                "review_text",
            ],
            reviews,
        ),
    ]

    for filename, headers, rows in files:
        with open(root / filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()

