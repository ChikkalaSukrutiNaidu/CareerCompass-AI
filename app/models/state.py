from typing import List, Optional
from pydantic import BaseModel, Field


# ==========================================================
# Student Profile
# ==========================================================

class StudentProfile(BaseModel):
    career_goal: str
    higher_studies: bool
    preferred_location: str
    preferred_work_style: str


# ==========================================================
# Job Offer
# ==========================================================

class Offer(BaseModel):
    company: str
    role: str
    ctc: float
    location: str


# ==========================================================
# Goal Agent Output
# ==========================================================

class GoalAnalysis(BaseModel):
    technology: int = Field(
        description="Importance of technology stack"
    )

    career_growth: int = Field(
        description="Importance of career growth"
    )

    salary: int = Field(
        description="Importance of salary"
    )

    work_life_balance: int = Field(
        description="Importance of work-life balance"
    )

    higher_studies: int = Field(
        description="Importance of higher studies"
    )

    reason: str = Field(
        description="Reason for assigning the priorities"
    )


# ==========================================================
# Offer Intelligence Agent Output
# ==========================================================

class OfferAnalysis(BaseModel):
    company: str

    technology: int = Field(description="Technology exposure score")

    career_growth: int = Field(description="Career growth score")

    salary: int = Field(description="Salary competitiveness score")

    learning: int = Field(description="Learning opportunities score")

    brand: int = Field(description="Brand value score")

    summary: str


# ==========================================================
# Preference Agent Output
# ==========================================================
class PreferenceAnalysis(BaseModel):

    company: str

    location_match: int = Field(
        ge=1,
        le=10,
        description="Location compatibility score (1-10)"
    )

    work_style_match: int = Field(
        ge=1,
        le=10,
        description="Work style compatibility score (1-10)"
    )

    higher_studies_support: int = Field(
        ge=1,
        le=10,
        description="Support for higher studies (1-10)"
    )

    summary: str


# ==========================================================
# Market Insight Agent Output
# ==========================================================

class MarketInsight(BaseModel):
    industry_trend: str
    future_scope: str
    summary: str


# ==========================================================
# Risk Agent Output
# ==========================================================

class RiskAnalysis(BaseModel):
    risks: List[str]
    summary: str

class DecisionEvaluation(BaseModel):
    best_offer: str

    strengths: List[str]

    tradeoffs: List[str]

    reasoning: str

# ==========================================================
# Final Recommendation
# ==========================================================
class ScoreBreakdown(BaseModel):
    technology: float
    career_growth: float
    salary: float
    location: float
    work_style: float
    higher_studies: float


class OfferScore(BaseModel):
    company: str
    total_score: float
    breakdown: ScoreBreakdown

class Recommendation(BaseModel):

    recommended_company: str = Field(
        description="Best company for the student"
    )

    final_score: float = Field(
        description="Overall score of the recommended offer"
    )

    strengths: List[str] = Field(
        description="Reasons why this offer is recommended"
    )

    tradeoffs: List[str] = Field(
        description="Things the student should consider"
    )

    runner_up: str = Field(
        description="Second best offer"
    )

    explanation: str = Field(
        description="Professional explanation of the recommendation"
    )


# ==========================================================
# Shared LangGraph State
# ==========================================================
class Scenario(BaseModel):
    """
    Stores user changes for What-If Analysis.
    """

    salary_priority: Optional[int] = None
    technology_priority: Optional[int] = None
    career_growth_priority: Optional[int] = None
    preferred_location: Optional[str] = None
    preferred_work_style: Optional[str] = None
    higher_studies: Optional[bool] = None


class ScenarioResult(BaseModel):
    """
    Stores comparison between original and new recommendation.
    """

    original_company: str
    new_company: str

    original_score: float
    new_score: float

    changed: bool

    explanation: str

class CareerCompassState(BaseModel):

    # User Details
    student: StudentProfile

    # Placement Offers
    offers: List[Offer]

    # Agent Outputs
    goal_analysis: Optional[GoalAnalysis] = None

    

    offer_analysis: Optional[List[OfferAnalysis]] = None

    preference_analysis: Optional[List[PreferenceAnalysis]] = None

    market_insight: Optional[MarketInsight] = None

    risk_analysis: Optional[RiskAnalysis] = None

    decision_evaluation: Optional[DecisionEvaluation] = None

    offer_scores: Optional[List[OfferScore]] = None

    recommendation: Optional[Recommendation] = None

    scenario: Optional[Scenario] = None

    scenario_result: Optional[ScenarioResult] = None