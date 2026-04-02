from fastapi import FastAPI
from env.environment import CodeReviewEnv

app = FastAPI()

env = CodeReviewEnv()

@app.get("/")
def root():
    return {"message": "Code Review OpenEnv API running"}

@app.post("/api/reset")
def reset(task: str = "easy"):
    observation = env.reset(task)
    return {"observation": observation}

@app.get("/api/state")
def state():
    return {"state": env.state}