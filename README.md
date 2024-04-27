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
2. Sales performance for each sales team by month?
3. Which sales channels contributed most to the company's revenue (In-Store, Online, Distributor, Wholesale)?
4. Warehouse Performance: What was the order volume handled by each warehouse, and how efficient was the processing from the order date to delivery?
5. What were the company's best-selling products?
6. Customer Relations: Which customers generated the highest number of orders and the most revenue?
