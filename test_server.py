#!/usr/bin/env python3
"""
Test script for the Code Review OpenEnv Environment
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_server():
    print("Testing Code Review OpenEnv Environment...")

    # Test root endpoint
    response = requests.get(f"{BASE_URL}/")
    print(f"Root endpoint: {response.json()}")

    # Test tasks endpoint
    response = requests.get(f"{BASE_URL}/tasks")
    print(f"Available tasks: {response.json()}")

    # Test each task
    tasks = ["easy", "medium", "hard"]
    test_reviews = {
        "easy": "The print statement is missing proper indentation",
        "medium": "This code is vulnerable to SQL injection attacks",
        "hard": "Using hardcoded passwords is a security risk"
    }

    for task in tasks:
        print(f"\n--- Testing {task.upper()} task ---")

        # Reset environment
        response = requests.get(f"{BASE_URL}/reset?task={task}")
        obs = response.json()["observation"]
        print(f"Code snippet: {obs['code_snippet']}")

        # Submit review
        review_data = {"review_comment": test_reviews[task]}
        response = requests.post(f"{BASE_URL}/step", json=review_data)
        result = response.json()
        print(f"Review: {test_reviews[task]}")
        print(f"Score: {result['reward']['score']}")
        print(f"Done: {result['done']}")

    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    test_server()