/*
Question: Which sales channels contributed most to the company's revenue (In-Store, Online, Distributor, Wholesale)?
*/

-- Total revenue generated by each sales channel
SELECT
    sales_channel,
    ROUND(SUM(order_revenue), 2) AS total_sales
FROM
    sales_data
GROUP BY
    sales_channel
ORDER BY
    total_sales DESC;

/*
JSON Results:
[
  {
    "sales_channel": "In-Store",
    "total_sales": "34040113.80"
  },
  {
    "sales_channel": "Online",
    "total_sales": "24629756.10"
  },
  {
    "sales_channel": "Distributor",
    "total_sales": "14809907.80"
  },
  {
    "sales_channel": "Wholesale",
    "total_sales": "9212948.90"
  }
]
*/