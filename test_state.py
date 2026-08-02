from app.models.sample_data import sample_state

print("\n===== Student Profile =====")
print(sample_state.student)

print("\n===== Placement Offers =====")

for offer in sample_state.offers:
    print(offer)

print("\n===== Initial State =====")
print(sample_state)