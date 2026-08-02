from langgraph.graph import StateGraph, START, END

from app.models.state import CareerCompassState

from app.agents.supervisor import supervisor_agent
from app.agents.goal_agent import goal_agent
from app.agents.offer_agent import offer_agent
from app.agents.preference_agent import preference_agent
from app.agents.recommendation_agent import recommendation_agent


workflow = StateGraph(CareerCompassState)

# Register Nodes
workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("goal", goal_agent)
workflow.add_node("offer", offer_agent)
workflow.add_node("preference", preference_agent)
workflow.add_node("recommendation", recommendation_agent)

# Connect Nodes
workflow.add_edge(START, "supervisor")
workflow.add_edge("supervisor", "goal")
workflow.add_edge("goal", "offer")
workflow.add_edge("offer", "preference")
workflow.add_edge("preference", "recommendation")
workflow.add_edge("recommendation", END)

graph = workflow.compile()