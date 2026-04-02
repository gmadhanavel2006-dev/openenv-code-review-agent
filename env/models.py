from pydantic import BaseModel


class Observation(BaseModel):
    code_snippet: str
    feedback: str | None = None


class Action(BaseModel):
    review_comment: str


class Reward(BaseModel):
    score: float