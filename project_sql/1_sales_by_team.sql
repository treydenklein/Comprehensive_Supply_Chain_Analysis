/*
Question: What were the total sales for each sales team over the given data's timeframe?
*/

-- Total amount of sales for each sales team
SELECT
    sales_team_id,
    SUM(order_revenue) AS total_sales
FROM
    sales_data
GROUP BY
    sales_team_id
ORDER BY
    total_sales DESC;

/*
JSON Results:
[
  {
    "sales_team_id": "26",
    "total_sales": "3346569.6"
  },
  {
    "sales_team_id": "1",
    "total_sales": "3261359.0"
  },
  {
    "sales_team_id": "13",
    "total_sales": "3242525.3"
  },
  {
    "sales_team_id": "8",
    "total_sales": "3228803.7"
  },
  {
    "sales_team_id": "11",
    "total_sales": "3217192.6"
  },
  {
    "sales_team_id": "19",
    "total_sales": "3191605.3"
  },
  {
    "sales_team_id": "12",
    "total_sales": "3181160.0"
  },
  {
    "sales_team_id": "24",
    "total_sales": "3098435.1"
  },
  {
    "sales_team_id": "21",
    "total_sales": "3050999.1"
  },
  {
    "sales_team_id": "18",
    "total_sales": "3043160.1"
  },
  {
    "sales_team_id": "7",
    "total_sales": "3036754.9"
  },
  {
    "sales_team_id": "15",
    "total_sales": "2996923.4"
  },
  {
    "sales_team_id": "9",
    "total_sales": "2993305.4"
  },
  {
    "sales_team_id": "16",
    "total_sales": "2974217.1"
  },
  {
    "sales_team_id": "22",
    "total_sales": "2946016.8"
  },
  {
    "sales_team_id": "3",
    "total_sales": "2923826.4"
  },
  {
    "sales_team_id": "20",
    "total_sales": "2910734.6"
  },
  {
    "sales_team_id": "23",
    "total_sales": "2884236.1"
  },
  {
    "sales_team_id": "25",
    "total_sales": "2819487.3"
  },
  {
    "sales_team_id": "2",
    "total_sales": "2814857.6"
  },
  {
    "sales_team_id": "4",
    "total_sales": "2802482.7"
  },
  {
    "sales_team_id": "14",
    "total_sales": "2771602.4"
  },
  {
    "sales_team_id": "10",
    "total_sales": "2764446.8"
  },
  {
    "sales_team_id": "5",
    "total_sales": "2762684.7"
  },
  {
    "sales_team_id": "17",
    "total_sales": "2757854.0"
  },
  {
    "sales_team_id": "6",
    "total_sales": "2630366.4"
  },
  {
    "sales_team_id": "27",
    "total_sales": "2535795.9"
  },
  {
    "sales_team_id": "28",
    "total_sales": "2505324.3"
  }
]
*/