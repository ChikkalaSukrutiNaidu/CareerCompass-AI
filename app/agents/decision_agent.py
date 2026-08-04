from app.services.llm_service import get_llm
from app.models.state import DecisionEvaluation
from app.prompts.decision_prompt import DECISION_PROMPT

llm = get_llm()


def decision_agent(state):

    structured_llm = llm.with_structured_output(DecisionEvaluation)

    prompt = f"""
{DECISION_PROMPT}

Goal Analysis:
{state.goal_analysis}

Offer Analysis:
{state.offer_analysis}

Preference Analysis:
{state.preference_analysis}
"""

    result = structured_llm.invoke(prompt)

    state.decision_evaluation = result

    print("✅ Decision Evaluation Completed")

    return state