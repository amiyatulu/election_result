import pandas as pd

json_file_path = "data/madhya_pradesh/constituency_data_all.json"

df = pd.read_json(json_file_path)

print(df)

# Vote wastage in the constituency

candidate_infos = df[df["Constituency"] == "Agar - 166"]["Candidates_info"]

won_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'won'])
print(won_candidates)

print(won_candidates.to_dict())

# df_json = won_candidates.to_json(orient='records', lines=True)
# print(df_json[0])