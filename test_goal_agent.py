from app.models.sample_data import sample_state
from app.agents.goal_agent import goal_agent

updated_state = goal_agent(sample_state)

print("\nGoal Analysis")
print(updated_state.goal_analysis)

print("\nTechnology Priority:")
print(updated_state.goal_analysis.technology)