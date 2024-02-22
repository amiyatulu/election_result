import pandas as pd
import json


# Assuming your data is in a CSV file named 'election_data.csv'
df = pd.read_csv('data/loksabha2019/Constituency_Wise_Detailed_Result_General Election_2019.csv', skiprows=2)

json_directory_path = "analysis_data/lokshabha2019/state_data/"

df.columns = df.columns.str.strip()


print(df.head())

# Group the data by State Name
grouped_data = df.groupby('State Name')

# Iterate through each group (state) and save it to a JSON file
for state, data in grouped_data:
    state_file_name = state.replace(" ", "_").lower() + '_data.json'
    num_constituencies = data["PC NAME"].nunique()
    print(state, num_constituencies)

    state_data = data.to_dict(orient='records')

    with open(json_directory_path + state_file_name, 'w') as json_file:
        json.dump(state_data, json_file, indent=2)

print("JSON files created for each state.")