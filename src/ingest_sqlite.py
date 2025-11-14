import csv
import sqlite3
from pathlib import Path
from typing import Iterable, Mapping

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "ecom.db"

CSV_FILES = {
    "products": ROOT / "products.csv",
    "customers": ROOT / "customers.csv",
    "orders": ROOT / "orders.csv",
    "order_items": ROOT / "order_items.csv",
    "reviews": ROOT / "reviews.csv",
}


def read_csv(path: Path) -> Iterable[Mapping[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def create_schema(cur: sqlite3.Cursor) -> None:
    cur.executescript(
        """
        PRAGMA foreign_keys = ON;

        DROP TABLE IF EXISTS reviews;
        DROP TABLE IF EXISTS order_items;
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS products;
        DROP TABLE IF EXISTS customers;

        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            sku TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            in_stock TEXT NOT NULL
        );

        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            signup_date TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL
        );

        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            total_amount REAL NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );

        CREATE TABLE order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            line_total REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );

        CREATE TABLE reviews (
            review_id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            review_date TEXT NOT NULL,
            rating INTEGER NOT NULL,
            review_text TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );
        """
    )


def insert_data(cur: sqlite3.Cursor) -> None:
    cur.executemany(
        """
        INSERT INTO products (product_id, sku, name, category, price, in_stock)
        VALUES (:product_id, :sku, :name, :category, :price, :in_stock)
        """,
        read_csv(CSV_FILES["products"]),
    )

    cur.executemany(
        """
        INSERT INTO customers (
            customer_id, first_name, last_name, email,
            signup_date, city, country
        ) VALUES (
            :customer_id, :first_name, :last_name, :email,
            :signup_date, :city, :country
        )
        """,
        read_csv(CSV_FILES["customers"]),
    )

    cur.executemany(
        """
        INSERT INTO orders (order_id, customer_id, order_date, total_amount, status)
        VALUES (:order_id, :customer_id, :order_date, :total_amount, :status)
        """,
        read_csv(CSV_FILES["orders"]),
    )

    cur.executemany(
        """
        INSERT INTO order_items (
            order_item_id, order_id, product_id, quantity, unit_price, line_total
        ) VALUES (
            :order_item_id, :order_id, :product_id, :quantity, :unit_price, :line_total
        )
        """,
        read_csv(CSV_FILES["order_items"]),
    )

    cur.executemany(
        """
        INSERT INTO reviews (
            review_id, product_id, customer_id, review_date, rating, review_text
        ) VALUES (
            :review_id, :product_id, :customer_id, :review_date, :rating, :review_text
        )
        """,
        read_csv(CSV_FILES["reviews"]),
    )


def create_indexes(cur: sqlite3.Cursor) -> None:
    cur.executescript(
        """
        CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
        CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items(order_id);
        CREATE INDEX IF NOT EXISTS idx_order_items_product ON order_items(product_id);
        CREATE INDEX IF NOT EXISTS idx_reviews_product ON reviews(product_id);
        CREATE INDEX IF NOT EXISTS idx_reviews_customer ON reviews(customer_id);
        """
    )


def main() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cur = conn.cursor()
        create_schema(cur)
        insert_data(cur)
        create_indexes(cur)
        conn.commit()
        print("Ingested CSVs into ecom.db")  # <-- This line shows success



if __name__ == "__main__":
    main()

