from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CodeReviewEnv

app = FastAPI()

env = CodeReviewEnv()


class ResetRequest(BaseModel):
    task: str = "easy"


@app.get("/")
def root():
    return {"message": "OpenEnv Code Review Agent API"}


@app.post("/api/reset")
def reset(req: ResetRequest):
    observation = env.reset(req.task)
    return {
        "observation": {
            "code_snippet": observation["code_snippet"],
            "feedback": None
        }
    }


@app.get("/api/state")
def state():
    return {"state": env.state}