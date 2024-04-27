-- Sales by month for each sales team id

SELECT
    sales_team_id,
    EXTRACT(MONTH FROM order_date) AS month,
    EXTRACT(YEAR FROM order_date) AS year,
    SUM(order_revenue) AS sales
FROM
    sales_data
GROUP BY
    year,
    month,
    sales_team_id
ORDER BY
    CAST(sales_team_id AS INT),
    year,
    month;

/*
Partial JSON Results:
[
  {
    "sales_team_id": "1",
    "month": "6",
    "year": "2018",
    "sales": "123313.5"
  },
  {
    "sales_team_id": "1",
    "month": "7",
    "year": "2018",
    "sales": "86041.4"
  },
  {
    "sales_team_id": "1",
    "month": "8",
    "year": "2018",
    "sales": "179727.5"
  },
  {
    "sales_team_id": "1",
    "month": "9",
    "year": "2018",
    "sales": "103381.0"
  },
  {
    "sales_team_id": "1",
    "month": "10",
    "year": "2018",
    "sales": "50430.9"
  },
  {
    "sales_team_id": "28",
    "month": "8",
    "year": "2020",
    "sales": "98925.5"
  },
  {
    "sales_team_id": "28",
    "month": "9",
    "year": "2020",
    "sales": "104104.6"
  },

  ...

  {
    "sales_team_id": "28",
    "month": "10",
    "year": "2020",
    "sales": "31007.6"
  },
  {
    "sales_team_id": "28",
    "month": "11",
    "year": "2020",
    "sales": "116365.6"
  },
  {
    "sales_team_id": "28",
    "month": "12",
    "year": "2020",
    "sales": "115307.0"
  }
]
*/