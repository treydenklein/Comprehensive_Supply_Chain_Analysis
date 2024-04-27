# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick  # Import ticker module

# Read the CSV file
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Supply_Chain_Analysis\csv_files\sales_by_channel.csv"
)

# Extract sales channels and total sales
sales_channels = df["sales_channel"]
total_sales = df["total_sales"]

# Create colormap going from dark to light
colors = plt.cm.Reds(np.linspace(0.2, 1, len(sales_channels)))
colors = colors[::-1]  # Reverse the order of colors

# Create bar chart
plt.style.use("dark_background")  # Set plot style to dark mode
plt.figure(figsize=(10, 6))
plt.barh(sales_channels, total_sales, color=colors)
plt.title("Total Sales by Sales Channel")
plt.xlabel("Total Sales")
plt.xticks(rotation=45)
plt.yticks(rotation=45)

# Format x-axis ticks with dollar sign ($)
fmt = "${x:,.0f}"
tick = mtick.StrMethodFormatter(fmt)
plt.gca().xaxis.set_major_formatter(tick)

plt.gca().invert_yaxis()  # Invert y-axis to display highest sales at the top

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Note: Saved as '...\assets\sales_by_channel_bar_chart.png'
