from app.services.llm_service import get_llm
from app.models.state import Scenario
from app.prompts.scenario_interpreter_prompt import (
    SCENARIO_INTERPRETER_PROMPT,
)

llm = get_llm()


def scenario_interpreter_agent(user_query: str):

    structured_llm = llm.with_structured_output(Scenario)

    prompt = f"""
{SCENARIO_INTERPRETER_PROMPT}

User Scenario:

{user_query}
"""

    result = structured_llm.invoke(prompt)

    print("✅ Scenario Interpreted")

    return result