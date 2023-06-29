# Import the pandas library
import pandas as pd

# Read the CSV files
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Perform the left outer join
merged_df = pd.merge(df1, df2, on='id', how='left')

# Write the merged DataFrame to a CSV file
merged_df.to_csv('merged_file.csv', index=False)

# Assuming we have three csv files: 'file1.csv', 'file2.csv' and 'file3.csv'
# And we want to join them on two common columns: 'id' and 'date'

# Read the csv files into pandas DataFrames
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')
df3 = pd.read_csv('file3.csv')

# Perform the first merge
merged_df = pd.merge(df1, df2, on=['id', 'date'], how='inner')

# Perform the second merge
final_merged_df = pd.merge(merged_df, df3, on=['id', 'date'], how='inner')

# Write the final merged DataFrame to a CSV file
final_merged_df.to_csv('merged_file.csv', index=False)

