import json

# Load the JSON data from the file
with open('analysis_data/lokshabha2019/seats/seats_by_party.json') as file:
    data = json.load(file)

# Dictionary to store total seats by party
total_seats_by_party = {}

# Iterate through the states and parties in the data
for state, parties in data.items():
    for party, seats in parties.items():
        # Add or update the total seats for each party
        total_seats_by_party[party] = total_seats_by_party.get(party, 0) + seats

# Save the total seats by party to a new JSON file
with open('analysis_data/lokshabha2019/seats/total_seats.json', 'w') as output_file:
    json.dump(total_seats_by_party, output_file, indent=2)

print("Total seats by party saved to 'total_seats_by_party.json'")
