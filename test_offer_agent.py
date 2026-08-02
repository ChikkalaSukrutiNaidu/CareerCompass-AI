from app.models.sample_data import sample_state
from app.agents.offer_agent import offer_agent

updated_state = offer_agent(sample_state)

print("\n===== Offer Analysis =====\n")

for analysis in updated_state.offer_analysis:
    print(analysis)
    print("-" * 50)