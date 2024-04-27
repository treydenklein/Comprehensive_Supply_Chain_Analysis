-- Upload data from CSV file into database table

COPY sales_data
FROM 'C:\Users\treyd\Projects\Data_Analytics\Data_Analysis_Portfolio_Projects\Supply_Chain_Analysis\csv_files\clean_sales_data.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');


/*
Database Load Issues (follow if receiving permission denied when running SQL code above)

NOTE: If you are having issues with permissions. And you get error: 

'could not open file "[your file path]\clean_sales_data.csv" for reading: Permission denied.'

1. Open pgAdmin
2. In Object Explorer (left-hand pane), navigate to `supply_chain_analysis` database
3. Right-click `supply_chain_analysis` and select `PSQL Tool`
    - This opens a terminal window to write the following code
4. Get the absolute file path of your csv file
    1. Find path by right-clicking a CSV file in VS Code and selecting “Copy Path”
5. Paste the following into `PSQL Tool`, (with the CORRECT file path)

\copy sales_data FROM '[your file path]\clean_sales_data.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');
*/