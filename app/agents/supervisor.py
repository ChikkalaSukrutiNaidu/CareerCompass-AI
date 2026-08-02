from app.services.llm_service import get_llm
from app.prompts.supervisor_prompt import SUPERVISOR_PROMPT

llm = get_llm()


def supervisor_agent(state):

    prompt = f"""
{SUPERVISOR_PROMPT}

Student Goal:
{state.student.career_goal}

Number of Offers:
{len(state.offers)}
"""

    response = llm.invoke(prompt)

    print("\n========== Supervisor ==========\n")
    print(response.content)

    return state