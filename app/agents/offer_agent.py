from app.services.llm_service import get_llm
from app.models.state import OfferAnalysis
from app.prompts.offer_prompt import OFFER_PROMPT

llm = get_llm()


def offer_agent(state):

    structured_llm = llm.with_structured_output(OfferAnalysis)

    analyses = []

    for offer in state.offers:

        prompt = f"""
{OFFER_PROMPT}

Company: {offer.company}

Role: {offer.role}

CTC: {offer.ctc} LPA

Location: {offer.location}
"""

        result = structured_llm.invoke(prompt)

        analyses.append(result)

        print(f"✅ Analyzed {offer.company}")

    state.offer_analysis = analyses

    return state