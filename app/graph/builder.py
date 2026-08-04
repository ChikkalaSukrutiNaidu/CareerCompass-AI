from langgraph.graph import StateGraph, START, END

from app.models.state import CareerCompassState

from app.agents.goal_agent import goal_agent
from app.agents.offer_agent import offer_agent
from app.agents.preference_agent import preference_agent
from app.scoring.score_engine import calculate_scores
from app.agents.recommendation_agent import recommendation_agent

workflow = StateGraph(CareerCompassState)

# Register Nodes
workflow.add_node("goal", goal_agent)
workflow.add_node("offer", offer_agent)
workflow.add_node("preference", preference_agent)
workflow.add_node("score", calculate_scores)
workflow.add_node("recommend", recommendation_agent)

# Connect Nodes
workflow.add_edge(START, "goal")
workflow.add_edge("goal", "offer")
workflow.add_edge("offer", "preference")
workflow.add_edge("preference", "score")
workflow.add_edge("score", "recommend")
workflow.add_edge("recommend", END)

graph = workflow.compile()