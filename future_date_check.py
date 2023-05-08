import pandas as pd
from datetime import datetime

# List of columns with date or datetime data
date_cols = ['DateColumn1', 'DateColumn2', 'DateTimeColumn']

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Check each column in the list for future dates
for col in date_cols:
    if df[col].dtype == 'datetime64[ns]':
        if (df[col] > datetime.now()).any():
            print(f"{col} column has future dates")
    elif df[col].dtype == 'object':
        try:
            date = pd.to_datetime(df[col], infer_datetime_format=True)
            if (date > datetime.now()).any():
                print(f"{col} column has future dates")
        except ValueError:
            pass
