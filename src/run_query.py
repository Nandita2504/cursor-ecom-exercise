import sqlite3
import pandas as pd

DB = "ecom.db"
ORDER_SQL_FILE = "order_summary.sql"
TOP_SQL_FILE = "top_customers.sql"

conn = sqlite3.connect(DB)

# ORDER SUMMARY
print("\n--- ORDER SUMMARY ---")
order_sql = open(ORDER_SQL_FILE, "r", encoding="utf-8").read()
df_order = pd.read_sql_query(order_sql, conn)
print(df_order.to_string(index=False))
df_order.to_csv("order_summary_output.csv", index=False)
print("Saved order_summary_output.csv")

# TOP CUSTOMERS
print("\n--- TOP CUSTOMERS ---")
top_sql = open(TOP_SQL_FILE, "r", encoding="utf-8").read()
df_top = pd.read_sql_query(top_sql, conn)
print(df_top.to_string(index=False))
df_top.to_csv("top_customers_output.csv", index=False)
print("Saved top_customers_output.csv")

conn.close()
