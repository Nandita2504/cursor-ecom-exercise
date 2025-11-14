# 🚀 E-Commerce Data Pipeline (Cursor IDE – A-SDLC Assignment)

This project demonstrates an end-to-end data workflow implemented using **Cursor IDE**, **Python**, and **SQLite**.  
The assignment involved generating synthetic e-commerce data, ingesting it into a SQLite database, and writing SQL queries that join multiple tables to produce meaningful insights.

The entire solution follows a clean project structure, clear prompts, and reproducible code — designed exactly as required in the assignment instructions.

---

## 📁 Project Structure

```
cursor-ecom-exercise/
│
├── data/
│   ├── products.csv
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── reviews.csv
│   ├── order_summary_output.csv
│   ├── top_customers_output.csv
│
├── src/
│   ├── ingest_sqlite.py
│   ├── run_query.py
│   ├── data_generator.py   (optional)
│
├── sql/
│   ├── order_summary.sql
│   ├── top_customers.sql
│
├── database/
│   ├── ecom.db
│
└── README.md
```

---

## 🧠 Prompts Used (Exactly as given during the assignment)

### 🟩 1. Prompt to Generate Synthetic E-Commerce Dataset
Hi — please create a small synthetic e-commerce dataset for my assignment. 
I need five CSV files of about 50 rows each: 
products.csv, customers.csv, orders.csv, order_items.csv, and reviews.csv.

Use realistic field names and types:

- products.csv: product_id, sku, name, category, price (two decimals), in_stock
- customers.csv: customer_id, first_name, last_name, email, signup_date (YYYY-MM-DD), city, country
- orders.csv: order_id, customer_id, order_date (YYYY-MM-DD), total_amount, status (completed/cancelled/refunded/pending)
- order_items.csv: order_item_id, order_id, product_id, quantity, unit_price, line_total
- reviews.csv: review_id, product_id, customer_id, review_date, rating (1-5), review_text

Make sure IDs match across files (no broken foreign keys).  
Output each CSV as a separate code block so I can save them.

---

### 🟩 2. Prompt to Create SQLite Ingestion Script
Write a Python script named `ingest_sqlite.py` that creates a SQLite database 
named `ecom.db`.

The script should:
- Create tables: products, customers, orders, order_items, reviews
- Set primary and foreign keys
- Read all 5 CSV files and insert rows into the database
- Enable foreign key constraints
- Add useful indexes for faster joins
- Print “Ingested CSVs into ecom.db” after completion

Return the full Python script.

---

### 🟩 3. Prompt to Generate Multi-Table JOIN SQL Query
Write an SQL query (for SQLite) that returns an order summary with:

- order_id
- order_date
- customer_name (first_name || ' ' || last_name)
- total_amount
- number_of_items (SUM of quantities)
- distinct_products (COUNT distinct product_id)
- top_product_name (product with highest line_total in that order)

Make sure the query uses JOINs and subqueries and works on SQLite.
Return only the SQL.

---

### 🟩 4. Prompt for "Top 10 Customers" SQL Query
Write an SQLite query that lists top 10 customers by total revenue 
(sum of orders.total_amount), including:

- customer_id
- customer_name
- total_revenue
- number_of_orders
- avg_order_value

Only include orders where status = 'completed'.
Return only the SQL.

---

## ⚙️ How to Run the Project

### 1️⃣ Install dependencies
`pip install pandas `

### 2️⃣ Ingest data
`python src/ingest_sqlite.py`

### 3️⃣ Run SQL Queries
`python src/run_query.py`

---
## Output
 
![Order Summary Screenshot](<Output 1.png>)
![Top Customers Screenshot](<Output 2.png>)



## 🙌 Author
Nandita Nair
