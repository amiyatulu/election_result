import json

# Read JSON data from file
with open('analysis_data/lokshabha2019/winners/winners.json', 'r') as json_file:
    data = json.load(json_file)

# Create a dictionary to store the count of seats by party for each state
seats_by_party = {}

# Iterate through each state in the data
for state, state_data in data.items():
    # Iterate through each PC Name in the state
    for pc_name, pc_result in state_data.items():
        # Extract the party of the winner
        winner_party = pc_result['Winner']['Party']

        # Update the count of seats for the party in the state
        if state not in seats_by_party:
            seats_by_party[state] = {}

        if winner_party not in seats_by_party[state]:
            seats_by_party[state][winner_party] = 1
        else:
            seats_by_party[state][winner_party] += 1

# Save the result to a JSON file
output_file_path = 'analysis_data/lokshabha2019/seats/seats_by_party.json'
with open(output_file_path, 'w') as output_file:
    json.dump(seats_by_party, output_file, indent=2)

print(f"Seats by Party saved to {output_file_path}")
