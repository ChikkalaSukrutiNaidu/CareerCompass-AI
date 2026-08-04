from app.services.llm_service import get_llm
from app.models.state import Recommendation
from app.prompts.recommendation_prompt import RECOMMENDATION_PROMPT

llm = get_llm()


def recommendation_agent(state):

    structured_llm = llm.with_structured_output(Recommendation)

    best = state.offer_scores[0]
    runner = state.offer_scores[1]

    prompt = f"""
{RECOMMENDATION_PROMPT}

Student Goal Analysis:
{state.goal_analysis}

Offer Analyses:
{state.offer_analysis}

Preference Analyses:
{state.preference_analysis}

Score Ranking:
{state.offer_scores}

Top Offer:
Company: {best.company}
Score: {best.total_score}

Runner Up:
Company: {runner.company}
Score: {runner.total_score}

IMPORTANT:
- Do NOT change the ranking.
- The recommended company MUST be {best.company}.
- The final score MUST be {best.total_score}.
- The runner-up company MUST be {runner.company}.
"""

    result = structured_llm.invoke(prompt)

    state.recommendation = result

    print("✅ Recommendation Generated")

    return state