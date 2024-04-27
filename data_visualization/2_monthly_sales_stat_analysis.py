# Import libraries
import pandas as pd

# Read CSV into pandas DataFrame
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Supply_Chain_Analysis\csv_files\team_monthly_sales.csv"
)

# Group by sales_team_id and calculate the standard deviation and variance of monthly sales
grouped = df.groupby("sales_team_id")
results = grouped["sales"].agg(["std", "var"])

# Rename and format columns for clarity
results.reset_index(
    inplace=True
)  # Reset index to turn 'sales_team_id' into a regular column
results.rename(
    columns={
        "sales_team_id": "Sales Team ID",
        "std": "Std Deviation",
        "var": "Variance",
    },
    inplace=True,
)

# Round the results to two decimal places
results = results.round(2)

# Display results
print("\nStd Deviation and Variance of Monthly Sales for Each Sales Team ID:\n")
print(results.to_string(index=False))
