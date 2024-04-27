# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Supply_Chain_Analysis\csv_files\performance_by_warehouse.csv"
)

# Extract warehouse codes, number of orders, and average processing times
warehouse_codes = df["warehouse_code"]
num_orders = df["num_orders"]
avg_processing_times = df["avg_processing_time"]

# Create figure to display bar charts
plt.style.use("dark_background")  # Set plot style to dark mode
plt.figure(figsize=(10, 6))

# Plot data for number of orders by warehouse
plt.subplot(2, 1, 1)  # 2 rows, 1 column, plot 1
plt.bar(warehouse_codes, num_orders, color="skyblue")
plt.title("Number of Orders by Warehouse")
plt.xlabel("Warehouse Code")
plt.ylabel("Number of Orders")

# Plot average processing time by warehouse
plt.subplot(2, 1, 2)  # 2 rows, 1 column, plot 2
bars = plt.bar(warehouse_codes, avg_processing_times, color="salmon")
plt.title("Avg Processing Time by Warehouse")
plt.xlabel("Warehouse Code")
plt.ylabel("Avg Processing Time (Days)")
plt.ylim(19, 22)  # Adjust y-axis range to make different bar heights clearer

# Add bar labels to average processing time chart
for bar in bars:
    yval = bar.get_height()  # Get the height of the bar (the value)
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        round(yval, 2),
        ha="center",
        va="bottom",
        fontsize=10,
    )

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Note: Saved as '...\assets\warehouse_performance.png'
