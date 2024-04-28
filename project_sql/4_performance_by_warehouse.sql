/*
Warehouse Performance: What was the order volume handled by each warehouse, and how efficient was the processing from the order date to delivery?
*/

-- Average order processing time (in days) and number of orders by warehouse
SELECT
    warehouse_code,
    COUNT(*) AS num_orders,
    ROUND(AVG(delivery_date - order_date), 2) AS avg_processing_time
FROM
    sales_data
GROUP BY
    warehouse_code
ORDER BY
    avg_processing_time DESC;

/*
JSON Results:
[
  {
    "warehouse_code": "WARE-NMK1003",
    "num_orders": "2505",
    "avg_processing_time": "20.96"
  },
  {
    "warehouse_code": "WARE-UHY1004",
    "num_orders": "1265",
    "avg_processing_time": "20.76"
  },
  {
    "warehouse_code": "WARE-NBV1002",
    "num_orders": "691",
    "avg_processing_time": "20.65"
  },
  {
    "warehouse_code": "WARE-PUJ1005",
    "num_orders": "1451",
    "avg_processing_time": "20.56"
  },
  {
    "warehouse_code": "WARE-XYS1001",
    "num_orders": "1222",
    "avg_processing_time": "20.40"
  },
  {
    "warehouse_code": "WARE-MKL1006",
    "num_orders": "857",
    "avg_processing_time": "20.30"
  }
]
*/