# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # Import ticker module

# Read CSV file
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Comprehensive_Supply_Chain_Analysis\csv_files\sales_by_team.csv"
)

# Extract sales team ids and total sales
sales_team_ids = df["sales_team_id"].astype(str)
total_sales = df["total_sales"]

# Calculate the average total sales
average_sales = total_sales.mean()

# Create bar chart
plt.style.use("dark_background")  # Set plot style to dark mode
plt.figure(figsize=(10, 6))

# Plot the average line
plt.axhline(y=average_sales, color="white", linestyle="--", label="Average Sales")

# Determine bar color based on value compared to average line
bar_color = [
    {value < average_sales: "grey", value > average_sales: "skyblue"}[True]
    for value in total_sales
]

# Plot data
plt.bar(sales_team_ids, total_sales, color=bar_color)

# Add text label for average plot line
plt.text(
    x=26.5,  # x-position
    y=average_sales + 20000,  # y-position
    s=f"${average_sales:,.0f}",  # Text to display
    color="white",
    ha="center",
    fontsize=11,
)

# Customize bar chart
plt.title("Total Sales by Team")
plt.xlabel("Sales Team ID")
plt.xticks(rotation=45)
plt.ylabel("Total Sales")
plt.yticks(rotation=45)
plt.ylim(2200000, 3400000)  # Adjust range of y-axis
plt.legend()  # Show chart legend

# Format y-axis ticks with dollar sign ($)
fmt = "${x:,.0f}"
tick = mtick.StrMethodFormatter(fmt)
plt.gca().yaxis.set_major_formatter(tick)

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Note: Saved as '...\assets\sales_by_team_id.png'
