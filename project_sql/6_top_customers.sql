-- Customer Relations: Which customers generated the highest number of orders and the most revenue?

-- Top 5 customers by total sales and number of orders
SELECT
    customer_id,
    COUNT(*) AS num_orders,
    SUM(order_revenue) AS total_sales
FROM
    sales_data
GROUP BY
    customer_id
ORDER BY
    total_sales DESC
LIMIT 5;

/*
JSON Results:
[
  {
    "customer_id": "12",
    "num_orders": "210",
    "total_sales": "2248332.4"
  },
  {
    "customer_id": "29",
    "num_orders": "179",
    "total_sales": "2112221.9"
  },
  {
    "customer_id": "17",
    "num_orders": "175",
    "total_sales": "1962014.6"
  },
  {
    "customer_id": "34",
    "num_orders": "176",
    "total_sales": "1937827.6"
  },
  {
    "customer_id": "33",
    "num_orders": "156",
    "total_sales": "1895188.8"
  }
]
*/