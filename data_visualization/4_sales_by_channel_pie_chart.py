# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Supply_Chain_Analysis\csv_files\sales_by_channel.csv"
)

# Group data by sales_channel and calculate the total sales for each channel
sales_by_channel = df.groupby("sales_channel")["total_sales"].sum()

# Plotting the pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    sales_by_channel,
    labels=sales_by_channel.index,
    autopct="%1.2f%%",
    startangle=140,
    wedgeprops={"edgecolor": "white", "linewidth": 1, "antialiased": True},
)
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle

# Title for the pie chart
plt.title("Percentage of Sales by Channel", pad=10)

plt.show()
# Note: Saved as '...\assets\sales_by_channel_pie_chart.png'
