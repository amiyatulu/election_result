import pandas as pd
import json
import numpy as np


# Assuming your data is in a CSV file named 'election_data.csv'
df = pd.read_csv('data/loksabha2019/Constituency_Wise_Detailed_Result_General Election_2019.csv', skiprows=2)

json_directory_path = "analysis_data/lokshabha2019/winners/"


df.columns = df.columns.str.strip()

# Convert int64 values to Python integers
df = df.applymap(lambda x: int(x) if isinstance(x, np.int64) else x)

# Group the data by State Name
grouped_data = df.groupby('State Name')

# Create a dictionary to store the results
result_dict = {}

# Iterate through each group (state)
for state, data in grouped_data:
    # Create a dictionary to store the results for each PC Name in the state
    state_result = {}

    # Group the data by PC Name within the state
    pc_grouped_data = data.groupby('PC NAME')

    # Iterate through each group (PC Name) in the state
    for pc_name, pc_data in pc_grouped_data:
        # Check if 'TOTAL' column is present in the DataFrame
        if 'TOTAL' in pc_data.columns:
            # Find the winning candidate and the first runner-up based on 'TOTAL' votes
            winner = pc_data.loc[pc_data['TOTAL'].idxmax()]
            
            # Sort the DataFrame based on 'TOTAL' votes in descending order
            pc_data_sorted = pc_data.sort_values(by='TOTAL', ascending=False)
            
            # Find the second row (runner-up) if it exists
            if len(pc_data_sorted) > 1:
                runner_up = pc_data_sorted.iloc[1].copy()  # Create a copy to avoid SettingWithCopyWarning
            else:
                runner_up = None

            # Convert int64 values to Python integers
            winner['TOTAL'] = int(winner['TOTAL'])
            if runner_up is not None:
                runner_up['TOTAL'] = int(runner_up['TOTAL'])

            # Store the information in the dictionary for the PC Name
            pc_result = {
                'Winner': {
                    'Candidate Name': winner['CANDIDATES NAME'],
                    'Party': winner['PARTY NAME'],
                    'Votes': winner['TOTAL']
                },
                'Runner-up': {
                    'Candidate Name': runner_up['CANDIDATES NAME'] if runner_up is not None else None,
                    'Party': runner_up['PARTY NAME'] if runner_up is not None else None,
                    'Votes': runner_up['TOTAL'] if runner_up is not None else None
                }
            }

            # Store the PC result in the state result dictionary
            state_result[pc_name] = pc_result

    # Store the state result dictionary in the main result dictionary
    result_dict[state] = state_result
with open(json_directory_path+ 'winners.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent=2)

print("Results saved to results.json")
