import json

# Read data from JSON file
with open('analysis_data/total_votes_by_party_data/total_votes_by_party_data_rajasthan_with_karanpur.json', 'r') as file:
    data = json.load(file)

# Calculate total votes
total_votes = sum(data['VotesByParty'].values())

# Calculate percentage votes for each party
percentage_votes_by_party = {party: (votes / total_votes) * 100 for party, votes in data['VotesByParty'].items()}

# Create a new dictionary with the results
result_data = {'PercentageVotesByParty': percentage_votes_by_party}

# Write results to a new JSON file
with open('analysis_data/total_percentage_by_party_data/percentage_rajathan_with_karanpur.json', 'w') as file:
    json.dump(result_data, file, indent=2)

print("Percentage votes by party calculated and saved to 'percentage_votes_data.json'.")
