from app.services.llm_service import get_llm
from app.models.state import ScenarioResult
from app.prompts.scenario_prompt import SCENARIO_PROMPT

llm = get_llm()


def scenario_agent(state):

    # If no scenario is provided, skip
    if state.scenario is None:
        print("ℹ️ No scenario provided.")
        return state

    structured_llm = llm.with_structured_output(ScenarioResult)

    original = state.recommendation

    prompt = f"""
{SCENARIO_PROMPT}

Original Recommendation:

Company: {original.recommended_company}

Score: {original.final_score}

Scenario Changes:

{state.scenario}

Assume the scoring engine has already recalculated the scores.

Explain whether the recommendation changes and why.
"""

    result = structured_llm.invoke(prompt)

    state.scenario_result = result

    print("✅ Scenario Analysis Completed")

    return state