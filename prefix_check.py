import pandas as pd

def check_prefixes(file_name):
    # Read the tab delimited file
    df = pd.read_csv(file_name, delimiter='\t')

    # Select the first column
    first_column = df.iloc[:, 0]

    # Initialize a dictionary to hold the counts of 'h', 'v', 'a', 'z'
    prefix_counts = {'h': 0, 'v': 0, 'a': 0, 'z': 0}

    # Iterate over the first column and count 'h', 'v', 'a', 'z'
    for value in first_column:
        if value in prefix_counts:
            prefix_counts[value] += 1

    # Check if 'h', 'v', 'a', 'z' each appear only once
    for prefix, count in prefix_counts.items():
        if count != 1:
            print(f"Prefix '{prefix}' appears {count} times. It should appear only once.")
            return False

    print("All prefixes appear only once.")
    return True
