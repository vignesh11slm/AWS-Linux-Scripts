import sys
import pandas as pd

def display_data_types(filename):
    try:
        data = pd.read_csv(filename)
        data_types = data.dtypes
        print(data_types)
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except pd.errors.EmptyDataError:
        print("The file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the file. Please ensure it is in a valid format.")

# Check if filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the filename as a command-line argument.")
else:
    filename = sys.argv[1]
    display_data_types(filename)
