from app.models.state import (
    CareerCompassState,
    StudentProfile,
    Offer
)

sample_state = CareerCompassState(

    student=StudentProfile(
        career_goal="AI Engineer",
        higher_studies=True,
        preferred_location="Hyderabad",
        preferred_work_style="Hybrid"
    ),

    offers=[

        Offer(
            company="Amazon",
            role="Software Development Engineer",
            ctc=28.5,
            location="Hyderabad"
        ),

        Offer(
            company="Microsoft",
            role="Software Engineer",
            ctc=32.0,
            location="Bangalore"
        ),

        Offer(
            company="Oracle",
            role="Associate Software Engineer",
            ctc=18.0,
            location="Hyderabad"
        )

    ],

    goal_analysis=None,
    offer_analysis=None,
    preference_analysis=None,
    market_insight=None,
    risk_analysis=None,
    recommendation=None
)