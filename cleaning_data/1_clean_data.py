# Import libraries
import pandas as pd
from dateutil import parser

# Read CSV file into pandas dataframe
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Supply_Chain_Analysis\original_csv_files\original_sales_data.csv"
)

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
df.to_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Supply_Chain_Analysis\clean_csv_files\clean_sales_data.csv",
    index=False,
)
