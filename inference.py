from env.environment import CodeReviewEnv
from env.models import Action


def simple_agent(code):

    if "range(10)\n" in code and ":" not in code:
        return "The for loop is missing a colon."

    if "SELECT" in code and "+" in code:
        return "Possible SQL injection vulnerability."

    if "password" in code:
        return "Hardcoded password detected."

    return "There may be a bug."


env = CodeReviewEnv()


def run_task(task):

    observation = env.reset(task)

    code = observation.code_snippet

    print("\nReviewing code:\n")
    print(code)

    review = simple_agent(code)

    print("\nAgent Review:\n", review)

    action = Action(review_comment=review)

    observation, reward, done, info = env.step(action)

    print("\nReward:", reward.score)
    print("Done:", done)


if __name__ == "__main__":

    for task in ["easy", "medium", "hard"]:
        run_task(task)