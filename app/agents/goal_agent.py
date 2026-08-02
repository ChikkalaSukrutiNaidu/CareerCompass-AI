from app.services.llm_service import get_llm
from app.models.state import GoalAnalysis
from app.prompts.goal_prompt import GOAL_PROMPT

llm = get_llm()


def goal_agent(state):

    structured_llm = llm.with_structured_output(GoalAnalysis)

    prompt = GOAL_PROMPT.format(
        career_goal=state.student.career_goal,
        higher_studies=state.student.higher_studies
    )

    result = structured_llm.invoke(prompt)

    state.goal_analysis = result

    print("\n✅ Goal Agent Completed\n")

    return state