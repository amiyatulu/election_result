import pandas as pd

json_file_path = "data/madhya_pradesh/constituency_data_all.json"

df = pd.read_json(json_file_path)

print(df)

# Vote wastage in the constituency

# NOTA votes

# Independent Votes



candidate_infos = df[df["Constituency"] == "Agar - 166"]["Candidates_info"]

won_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'won'])
print(won_candidates)
winner_info = won_candidates.iloc[0]

print(winner_info[0])
print(winner_info[0]["Candidate Name"])
print(winner_info[0]["Votes"])

lost_candidates = candidate_infos.apply(lambda x: [candidate for candidate in x if candidate['Status'] == 'lost'])
print(lost_candidates)

lost_candidates_votes = lost_candidates.apply(lambda x: [item['Votes'] for item in x])

print(lost_candidates_votes)
total_sum = sum(map(int, lost_candidates_votes.sum()))
print(total_sum)
# lost_candidate_dict = lost_candidates_votes.to_dict()

# numeric_values = list(map(int, lost_candidate_dict[0]))

# total_sum = sum(numeric_values)

# # Display the result
# print(f"Sum of the values: {total_sum}")


# print(lost_candidates.to_numeric(df['Votes'], errors="coerce"))

# df['Total Votes'] = df['Votes'].sum()


# print(df['Total Votes'].to_dict())


# df_json = won_candidates.to_json(orient='records', lines=True)
# print(df_json[0])