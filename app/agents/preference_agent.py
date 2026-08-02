from app.services.llm_service import get_llm
from app.models.state import PreferenceAnalysis
from app.prompts.preference_prompt import PREFERENCE_PROMPT

llm = get_llm()


def preference_agent(state):

    structured_llm = llm.with_structured_output(PreferenceAnalysis)

    analyses = []

    for offer in state.offers:

        prompt = PREFERENCE_PROMPT.format(
            location=state.student.preferred_location,
            work_style=state.student.preferred_work_style,
            higher_studies=state.student.higher_studies,
            company=offer.company,
            offer_location=offer.location,
        )

        result = structured_llm.invoke(prompt)

        analyses.append(result)

        print(f"✅ Preference analyzed for {offer.company}")

    state.preference_analysis = analyses

    return state