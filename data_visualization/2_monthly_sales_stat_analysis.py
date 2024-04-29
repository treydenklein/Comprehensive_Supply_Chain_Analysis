# Import libraries
import pandas as pd

# Read CSV into pandas DataFrame
df = pd.read_csv(
    r"C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Comprehensive_Supply_Chain_Analysis\csv_files\team_monthly_sales.csv"
)

# Group data by sales team ids
grouped = df.groupby("sales_team_id")["sales"]

# Calculate and format the mean, standard deviation, and variance of each team's monthly sales data
mean = grouped.mean().apply(lambda x: round(x, 2))
std_deviation = grouped.std().apply(lambda x: round(x, 2))
variance = grouped.var().apply(
    lambda x: "{:.4e}".format(x)
)  # Format variance in scientific notation

# Create new DataFrame to store the results
results = pd.DataFrame(
    {
        "sales_team_id": std_deviation.index,
        "mean": mean.values,
        "std_deviation": std_deviation.values,
        "variance": variance.values,
    }
)

# Ensure that the sales team ids are stored as strings while maintaining the order of the data
results["sales_team_id"] = results["sales_team_id"].astype(str)

# Store the results as a dictionary
results_dict = results.to_dict(
    orient="records"
)  # 'records' gives a list of dictionaries

# Print results to verify
print(results_dict)

# Results:
#    [
#        {
#            'sales_team_id': '1',
#            'mean': 105205.13,
#            'std_deviation': 54894.37,
#            'variance': '3.0134e+09'
#        },
#        {
#            'sales_team_id': '2',
#            'mean': 90801.86,
#            'std_deviation': 34954.17,
#            'variance': '1.2218e+09'
#        },
#        {
#            'sales_team_id': '3',
#            'mean': 94316.98,
#            'std_deviation': 47533.47,
#            'variance': '2.2594e+09'
#        },
#        {
#            'sales_team_id': '4',
#            'mean': 90402.67,
#            'std_deviation': 41641.02,
#            'variance': '1.7340e+09'
#        },
#        {
#            'sales_team_id': '5',
#            'mean': 89118.86,
#            'std_deviation': 40672.74,
#            'variance': '1.6543e+09'
#        },
#        {
#            'sales_team_id': '6',
#            'mean': 82198.95,
#            'std_deviation': 39696.13,
#            'variance': '1.5758e+09'
#        },
#        {
#            'sales_team_id': '7',
#            'mean': 97959.84,
#            'std_deviation': 41221.0,
#            'variance': '1.6992e+09'
#        },
#        {
#            'sales_team_id': '8',
#            'mean': 104154.96,
#            'std_deviation': 38546.38,
#            'variance': '1.4858e+09'
#        },
#        {
#            'sales_team_id': '9',
#            'mean': 96558.24,
#            'std_deviation': 50989.43,
#            'variance': '2.5999e+09'
#        },
#        {
#            'sales_team_id': '10',
#            'mean': 86388.96,
#            'std_deviation': 41906.5,
#            'variance': '1.7562e+09'
#        },
#        {
#            'sales_team_id': '11',
#            'mean': 103780.41,
#            'std_deviation': 51403.13,
#            'variance': '2.6423e+09'
#        },
#        {
#            'sales_team_id': '12',
#            'mean': 99411.25,
#            'std_deviation': 57711.99,
#            'variance': '3.3307e+09'
#        },
#        {
#            'sales_team_id': '13',
#            'mean': 104597.59,
#            'std_deviation': 45366.97,
#            'variance': '2.0582e+09'
#        },
#        {
#            'sales_team_id': '14',
#            'mean': 86612.57,
#            'std_deviation': 43566.08,
#            'variance': '1.8980e+09'
#        },
#        {
#            'sales_team_id': '15',
#            'mean': 96674.95,
#            'std_deviation': 53800.94,
#            'variance': '2.8945e+09'
#        },
#        {
#            'sales_team_id': '16',
#            'mean': 95942.49,
#            'std_deviation': 41389.63,
#            'variance': '1.7131e+09'
#        },
#        {
#            'sales_team_id': '17',
#            'mean': 88963.03,
#            'std_deviation': 42508.36,
#            'variance': '1.8070e+09'
#        },
#        {
#            'sales_team_id': '18',
#            'mean': 98166.45,
#            'std_deviation': 35719.22,
#            'variance': '1.2759e+09'
#        },
#        {
#            'sales_team_id': '19',
#            'mean': 102955.01,
#            'std_deviation': 47872.97,
#            'variance': '2.2918e+09'
#        },
#        {
#            'sales_team_id': '20',
#            'mean': 93894.66,
#            'std_deviation': 47121.04,
#            'variance': '2.2204e+09'
#        },
#        {
#            'sales_team_id': '21',
#            'mean': 95343.72,
#            'std_deviation': 39443.65,
#            'variance': '1.5558e+09'
#        },
#        {
#            'sales_team_id': '22',
#            'mean': 92063.02,
#            'std_deviation': 49656.77,
#            'variance': '2.4658e+09'
#        },
#        {
#            'sales_team_id': '23',
#            'mean': 93039.87,
#            'std_deviation': 46604.17,
#            'variance': '2.1719e+09'
#        },
#        {
#            'sales_team_id': '24',
#            'mean': 99949.52,
#            'std_deviation': 47511.02,
#            'variance': '2.2573e+09'
#        },
#        {
#            'sales_team_id': '25',
#            'mean': 90951.2,
#            'std_deviation': 51670.45,
#            'variance': '2.6698e+09'
#        },
#        {
#            'sales_team_id': '26',
#            'mean': 107953.86,
#            'std_deviation': 50256.74,
#            'variance': '2.5257e+09'
#        },
#        {
#            'sales_team_id': '27',
#            'mean': 81799.87,
#            'std_deviation': 40029.39,
#            'variance': '1.6024e+09'
#        },
#        {
#            'sales_team_id': '28',
#            'mean': 78291.38,
#            'std_deviation': 34181.64,
#            'variance': '1.1684e+09'
#        }
#    ]
