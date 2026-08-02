from app.models.sample_data import sample_state
from app.agents.preference_agent import preference_agent

updated = preference_agent(sample_state)

print("\n===== Preference Analysis =====\n")

for item in updated.preference_analysis:
    print(item)
    print("-" * 50)