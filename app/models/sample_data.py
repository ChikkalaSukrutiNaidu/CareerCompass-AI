from app.models.state import *

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

            role="SDE",

            ctc=28,

            location="Hyderabad"

        ),

        Offer(

            company="Microsoft",

            role="Software Engineer",

            ctc=32,

            location="Bangalore"

        )

    ]

)