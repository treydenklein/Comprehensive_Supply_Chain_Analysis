-- Top 5 best-selling products by total quantity sold
SELECT
    product_id,
    SUM(order_quantity) AS total_quantity_sold
FROM
    sales_data
GROUP BY
    product_id
ORDER BY
    total_quantity_sold DESC
LIMIT 5;

/*
JSON Results:
[
  {
    "product_id": "23",
    "total_quantity_sold": "956"
  },
  {
    "product_id": "37",
    "total_quantity_sold": "896"
  },
  {
    "product_id": "8",
    "total_quantity_sold": "879"
  },
  {
    "product_id": "4",
    "total_quantity_sold": "878"
  },
  {
    "product_id": "40",
    "total_quantity_sold": "855"
  }
]
*/