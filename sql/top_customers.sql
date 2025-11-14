SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    SUM(o.total_amount) AS total_revenue,
    COUNT(o.order_id) AS number_of_orders,
    AVG(o.total_amount) AS avg_order_value
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id
WHERE o.status = 'completed'
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_revenue DESC, customer_name
LIMIT 10;