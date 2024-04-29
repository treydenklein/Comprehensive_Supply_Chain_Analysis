# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # Import ticker module

# Read CSV file
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Comprehensive_Supply_Chain_Analysis\csv_files\top_5_customers.csv"
)

# Extract customer ids, number of orders, and total sales
customer_ids = df["customer_id"].astype(str)
num_orders = df["num_orders"]
total_sales = df["total_sales"]

# Create bar charts
plt.style.use("dark_background")  # Set plot style to dark mode
plt.figure(figsize=(10, 6))

# Plot sales
plt.subplot(2, 1, 1)
plt.bar(customer_ids, total_sales, color="salmon")
plt.title("Total Sales by Customer")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")

# Format y-axis ticks with dollar sign ($)
fmt = "${x:,.0f}"
tick = mtick.StrMethodFormatter(fmt)
plt.gca().yaxis.set_major_formatter(tick)

# Plot orders
plt.subplot(2, 1, 2)
plt.bar(customer_ids, num_orders, color="skyblue")
plt.title("Number of Orders by Customer")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Note: Saved as '...\assets\top_customers.png'
