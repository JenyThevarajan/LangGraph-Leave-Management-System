DEPLOYMENT_PROMPT = """
You are a DevOps Engineer.

Based on:

{design}

Generate:

1. Dockerfile

2. docker-compose.yml

3. requirements.txt

4. README.md

5. Run Instructions

Return markdown.
"""