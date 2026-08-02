from app.services.llm_service import get_llm
from app.prompts.goal_prompt import GOAL_PROMPT


llm = get_llm()


def goal_agent(state):

    prompt = f"""
    {GOAL_PROMPT}

    Student Goal:

    {state["student_goal"]}
    """

    response = llm.invoke(prompt)

    state["goal_analysis"] = response.content

    return state