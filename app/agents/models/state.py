from typing import TypedDict, List, Dict, Optional


class CareerCompassState(TypedDict):
    """
    Shared state passed between all LangGraph agents.
    """

    # User Information
    student_goal: str
    higher_studies: bool
    preferred_location: str
    preferred_work_style: str

    # Placement Offers
    offers: List[Dict]

    # Agent Outputs
    goal_analysis: Optional[Dict]
    offer_analysis: Optional[Dict]
    preference_analysis: Optional[Dict]

    # Final Output
    recommendation: Optional[Dict]