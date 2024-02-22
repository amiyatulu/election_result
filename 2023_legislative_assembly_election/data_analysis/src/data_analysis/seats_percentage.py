# Given seat counts
# seat_counts = {
#     "BJP": 163,
#     "INC": 66,
#     "BHRTADVSIP": 1
# }

seat_counts = {
    "BJP": 115,
    "INC": 70,
    "BHRTADVSIP": 3,
    "BSP":2,
    "RLD": 1,
    "RLTP": 1,
    "IND": 8,
}


# seat_counts = {
#     "BHRS": 39,
#     "INC": 64,
#     "BJP": 8,
#     "AIMIM": 7,
#     "CPI":1
# }

# Total number of seats
total_seats = sum(seat_counts.values())

# Calculate percentage for each party
percentage_seats = {party: (seats / total_seats) * 100 for party, seats in seat_counts.items()}

print("Percentage of Seats:")
for party, percentage in percentage_seats.items():
    print(f"{party}: {percentage:.2f}%")