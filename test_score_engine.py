from app.models.sample_data import sample_state

from app.agents.goal_agent import goal_agent
from app.agents.offer_agent import offer_agent
from app.agents.preference_agent import preference_agent

from app.scoring.score_engine import calculate_scores


state = goal_agent(sample_state)
state = offer_agent(state)
state = preference_agent(state)

state = calculate_scores(state)

print("\n===== SCORES =====\n")

for score in state.offer_scores:
    print(score)