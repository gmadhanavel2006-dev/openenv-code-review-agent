from fastapi import FastAPI
from env.environment import CodeReviewEnv

app = FastAPI()

# Create environment
environment = CodeReviewEnv()


@app.get("/")
def root():
    return {"message": "Code Review OpenEnv API running"}


@app.get("/api/reset")
def reset(task: str = "easy"):
    observation = environment.reset(task)
    return {"observation": observation}


@app.get("/api/state")
def state():
    return {"state": environment.state}