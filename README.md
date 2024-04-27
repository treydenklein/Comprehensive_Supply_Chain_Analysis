# Introduction

- This Project Explores and Analyzes Supply Chain Data for a Fictional Company
- Investigating:
  - 📈 Sales Team Performance
  - 📊 Various Sales Channels
  - 📦 Warehouse Performance
  - 🔥 Best-Selling Products
  - 🤝 Customer Relations

# The Tools I Used

- **SQL:** Running queries on the project database and revealing initial insights
- **Python:** Data Cleaning, Data Visualization, and Statistical Analysis
  - **Libraries:** Pandas, Numpy, Matplotlib
- **PostgreSQL:** Database management system
- **Tableau:** Building an Interactive Sales Dashboard
- **Visual Studio Code:** My preferred IDE for project management and executing scripts in various programming languages
- **Git & GitHub:** Version control, project tracking, and sharing my scripts + analysis

### Cleaning the Original Data

```python
# Import libraries
import pandas as pd

# Read CSV file into pandas dataframe
df = pd.read_csv(r"[file path]\csv_files\original_sales_data.csv")

# Set pandas to display all columns
pd.set_option("display.max_columns", None)

# Check dataframe for missing data
# Note: No data is missing in CSV file
missing_data = df.isnull().any()

# Check dataframe for duplicates
# Note: CSV file does not contain any duplicates
duplicates = df[df.duplicated()]

# Remove unnecessary columns
df.drop(columns=["Discount Applied", "CurrencyCode"], inplace=True)

# Rename columns for future SQL queries
modified_column_names = {
    "OrderNumber": "order_number",
    "Sales Channel": "sales_channel",
    "WarehouseCode": "warehouse_code",
    "ProcuredDate": "procured_date",
    "OrderDate": "order_date",
    "ShipDate": "ship_date",
    "DeliveryDate": "delivery_date",
    "_SalesTeamID": "sales_team_id",
    "_CustomerID": "customer_id",
    "_StoreID": "store_id",
    "_ProductID": "product_id",
    "Order Quantity": "order_quantity",
    "Unit Cost": "unit_cost",
    "Unit Price": "unit_price",
}
df.rename(columns=modified_column_names, inplace=True)

# Convert date columns to dtype: datetime with standard format YYYY-MM-DD
date_columns = ["procured_date", "order_date", "ship_date", "delivery_date"]
for column in date_columns:
    df[column] = pd.to_datetime(df[column], format="mixed", dayfirst=True)

# Convert pricing columns to dtype: float for future calculations
price_columns = ["unit_cost", "unit_price"]
for column in price_columns:
    df[column] = df[column].str.replace(r"[$,]", "", regex=True).astype(float).round(2)

# Convert ID columns from dtype: int to dtype: str
id_columns = ["sales_team_id", "customer_id", "store_id", "product_id"]
for column in id_columns:
    df[column] = df[column].astype(str)

# Calculate and display cost of each order
# Note: Will be stored as dtype: float
df["order_cost"] = (df["order_quantity"] * df["unit_cost"]).round(2)

# Calculate and display revenue from each order
# Note: Will be stored as dtype: float
df["order_revenue"] = (df["order_quantity"] * df["unit_price"]).round(2)

# Calculate and display profit from each order
# Note: Will be stored as dtype: float
df["order_profit"] = (df["order_revenue"] - df["order_cost"]).round(2)

# Write dataframe to CSV file
df.to_csv(r"[file path]\csv_files\clean_sales_data.csv", index=False)
```

### Initial SQL Queries - Questions to Answer:

1. What were the total sales for each sales team over the given data's timeframe?
2. How did each sales team perform month-over-month?
3. Which sales channels contributed most to the company's revenue (In-Store, Online, Distributor, Wholesale)?
4. Warehouse Performance: What was the order volume handled by each warehouse, and how efficient was the processing from the order date to delivery?
5. What were the company's best-selling products?
6. Customer Relations: Which customers generated the highest number of orders and the most revenue?

# Analysis

### 1. Total Sales for Each Sales Team

SQL Query:

- Group data by Sales Team ID
- Calculate the sum of each order's revenue to find the total amount of sales
- Order by the total amount of sales in descending order

```sql
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
```

Here is a breakdown of the results:

- **Top Sales Teams:** The top 5 sales teams in terms of total sales are teams 26, 1, 13, 8, and 11...all with totals over $3.2 million
- **Sales Discrepancy:** There is a significant difference in total sales between the highest and lowest performing sales teams. The top sales team (Team 26) has a total that is over $1,000,000 more than the lowest sales team (Team 28)
- **Middle of the Pack:** A majority of the sales teams have totals between $2.7 and $3.3 million
- **Overall Sales Performance:** The cumulative total sales amounts to approximately $87.2 million, indicating a strong overall performance across all teams

![Total Sales by Team](assets/sales_by_team_id.png)
_Bar graph visualizing the total amount of sales for each sales team, comparing each to the graph's average value_

### 2. Monthly Sales Performance by Sales Team ID

SQL Query:

- Group data by the sales team id, month, and year
- Calculate the sum of each order's revenue to find the total amount of sales for the month
- Order by the sales team id, year, and month to make results more readable

```sql
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
```

Here is a breakdown of the results:

- **Overall Sales Trends:** There are fluctuations in sales volumes over time, likely influenced by seasonality, economic factors, and team performance. Notable dips and spikes may indicate specific events or strategies impacting sales.
- **Seasonality Patterns:** For many sales teams, there is an observable pattern where sales tend to increase towards the end of the year, possibly due to holiday seasons, followed by a drop at the beginning of the new year.
- **High-Performing Sales Teams:** Teams with consistently high sales over multiple months or years can be identified. Understanding what contributes to their success might be valuable for other teams. Also, teams with signigicant spikes in sales may have launched successful campaigns or promotions.
- **Underperforming Sales Teams:** Teams with consistently low sales or frequent dips may require further analysis to understand the root causes. This could be due to staffing, market conditions, or other factors.
