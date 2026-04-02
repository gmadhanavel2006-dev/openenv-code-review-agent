# Code Review OpenEnv Environment

## Description
This project simulates a real-world code review task where an AI agent analyzes code and identifies bugs or security issues.

## Tasks
The environment includes three tasks:

1. Easy – detect syntax errors
2. Medium – detect SQL injection vulnerability
3. Hard – detect hardcoded password security issue

## Observation Space
The agent receives a code snippet that must be reviewed.

## Action Space
The agent outputs a text review comment describing issues in the code.

## Reward Function
Reward is based on correctness of the review.

Score range:
0.0 – incorrect  
0.5 – partially correct  
1.0 – correct identification

## Running the Project

Install dependencies:
