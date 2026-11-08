import re

from llm import llm
from prompts.reviewer_prompt import REVIEWER_PROMPT

def reviewer(state):

    prompt = REVIEWER_PROMPT.format(
        design=state["code_design"]
    )

    response = llm.invoke(prompt)

    text = response.content

    score = 80

    try:

        match = re.search(r"SCORE:\s*(\d+)", text)

        if match:
            score = int(match.group(1))

    except:
        pass

    return {
        "review_report": text,
        "review_score": score
    }