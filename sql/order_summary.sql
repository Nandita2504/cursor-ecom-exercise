
SELECT
    o.order_id,
    o.order_date,
    c.first_name || ' ' || c.last_name AS customer_name,
    o.total_amount,
    SUM(oi.quantity) AS number_of_items,
    COUNT(DISTINCT oi.product_id) AS distinct_products,
    (
        SELECT p2.name
        FROM order_items AS oi2
        JOIN products AS p2 ON p2.product_id = oi2.product_id
        WHERE oi2.order_id = o.order_id
        ORDER BY oi2.line_total DESC, p2.name
        LIMIT 1
    ) AS top_product_name
FROM orders AS o
JOIN customers AS c ON c.customer_id = o.customer_id
JOIN order_items AS oi ON oi.order_id = o.order_id
GROUP BY
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    o.total_amount
ORDER BY o.order_date, o.order_id;
