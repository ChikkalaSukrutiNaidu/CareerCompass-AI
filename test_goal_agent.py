from app.agents.goal_agent import goal_agent

state = {
    "student_goal": "Become an AI Engineer",
    "higher_studies": True,
    "preferred_location": "Hyderabad",
    "preferred_work_style": "Hybrid",
    "offers": [],
    "goal_analysis": None,
    "offer_analysis": None,
    "preference_analysis": None,
    "recommendation": None
}

updated_state = goal_agent(state)

print(updated_state["goal_analysis"])