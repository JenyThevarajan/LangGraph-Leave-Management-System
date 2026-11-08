REVIEWER_PROMPT = """
You are a Principal Engineer.

Review this code design.

{design}

Provide:

1. Score out of 100
2. Security Findings
3. Performance Findings
4. Recommended Fixes

Format:

SCORE: XX

Review:
...
"""