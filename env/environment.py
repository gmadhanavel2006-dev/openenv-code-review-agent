from env.tasks import tasks
from env.grader import grade_review
from env.models import Observation, Action, Reward


class CodeReviewEnv:

    def __init__(self):
        self.current_task = None
        self.done = False

    def reset(self, task="easy"):

        self.current_task = tasks[task]
        self.done = False

        observation = Observation(
            code_snippet=self.current_task["code"],
            feedback=None
        )

        return observation

    def step(self, action: Action):

        review = action.review_comment

        score = grade_review(review, self.current_task["solution"])

        reward = Reward(score=score)

        self.done = score == 1.0

        observation = Observation(
            code_snippet=self.current_task["code"],
            feedback=review
        )

        return observation, reward, self.done, {}

    def state(self):

        return {
            "task": self.current_task,
            "done": self.done
        }