# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Comprehensive_Supply_Chain_Analysis\csv_files\top_5_best_selling_products.csv"
)

# Extract product ids and total quantities sold
product_ids = df["product_id"].astype(str)
quantities = df["total_quantity_sold"]

# Create colormap going from dark to light
colors = plt.cm.Blues(np.linspace(0.2, 1, len(product_ids)))
colors = colors[::-1]  # Reverse the order of colors

# Create bar chart
plt.style.use("dark_background")  # Set plot style to dark mode
plt.figure(figsize=(10, 6))
plt.barh(product_ids, quantities, color=colors)
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product ID")
plt.title("Top 5 Best-Selling Products by Quantity Sold")
plt.gca().invert_yaxis()  # Invert y-axis to display highest quantity at the top

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Note: Saved as '...\assets\best_selling_products.png'
