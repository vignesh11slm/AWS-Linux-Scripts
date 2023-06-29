# Import the pandas library
import pandas as pd

# Read the CSV files
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Perform the left outer join
merged_df = pd.merge(df1, df2, on='id', how='left')

# Write the merged DataFrame to a CSV file
merged_df.to_csv('merged_file.csv', index=False)
