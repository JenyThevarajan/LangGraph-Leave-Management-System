CODE_GENERATOR_PROMPT = """
You are a Senior Python FastAPI Engineer.

Use the following information.

Requirements:
{requirements}

Architecture:
{architecture}

Design:
{design}

Generate:

1. Project Structure

2. Complete FastAPI Code

3. Models

4. Routers

5. Services

6. Database Configuration

7. Sample APIs

Return markdown with code blocks.
"""