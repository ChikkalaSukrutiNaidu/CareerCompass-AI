from typing import TypedDict, List, Dict, Optional


class Offer(TypedDict):
    company: str
    role: str
    ctc: float
    location: str


class CareerCompassState(TypedDict):
    # User Input
    student_goal: str
    higher_studies: bool
    preferred_location: str
    preferred_work_style: str

    # Placement Offers
    offers: List[Offer]

    # Agent Outputs
    goal_analysis: Optional[Dict]
    offer_analysis: Optional[Dict]
    preference_analysis: Optional[Dict]

    # Final Recommendation
    recommendation: Optional[Dict]