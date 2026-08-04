from app.models.state import OfferScore


def calculate_scores(state):

    scores = []

    goal = state.goal_analysis

    for offer, analysis, preference in zip(
        state.offers,
        state.offer_analysis,
        state.preference_analysis,
    ):

        technology = analysis.technology * goal.technology
        growth = analysis.career_growth * goal.career_growth
        salary = analysis.salary * goal.salary

        location = preference.location_match * 5
        workstyle = preference.work_style_match * 3
        higher = preference.higher_studies_support * 2

        total = (
            technology
            + growth
            + salary
            + location
            + workstyle
            + higher
        )

        scores.append(
            OfferScore(
                company=offer.company,
                total_score=total,
                breakdown={
                    "technology": technology,
                    "career_growth": growth,
                    "salary": salary,
                    "location": location,
                    "work_style": workstyle,
                    "higher_studies": higher,
                },
            )
        )

    state.offer_scores = sorted(
        scores,
        key=lambda x: x.total_score,
        reverse=True,
    )

    return state