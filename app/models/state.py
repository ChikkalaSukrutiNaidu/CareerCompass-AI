from typing import List, Optional, Dict
from pydantic import BaseModel, Field


# ----------------------------
# Job Offer Model
# ----------------------------

class Offer(BaseModel):
    company: str
    role: str
    ctc: float
    location: str


# ----------------------------
# Student Profile
# ----------------------------

class StudentProfile(BaseModel):
    career_goal: str
    higher_studies: bool
    preferred_location: str
    preferred_work_style: str


# ----------------------------
# Goal Agent Output
# ----------------------------

class GoalAnalysis(BaseModel):
    priorities: Dict[str, int]
    reason: str


# ----------------------------
# Offer Agent Output
# ----------------------------

class OfferAnalysis(BaseModel):
    company_scores: Dict[str, Dict]
    summary: str


# ----------------------------
# Recommendation Output
# ----------------------------

class Recommendation(BaseModel):
    recommended_company: str
    confidence_score: float
    explanation: str


# ----------------------------
# LangGraph State
# ----------------------------

class CareerCompassState(BaseModel):

    student: StudentProfile

    offers: List[Offer]

    goal_analysis: Optional[GoalAnalysis] = None

    offer_analysis: Optional[OfferAnalysis] = None

    recommendation: Optional[Recommendation] = None