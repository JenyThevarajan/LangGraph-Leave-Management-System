from llm import llm
from prompts.qa_prompt import QA_PROMPT

def qa(state):

    prompt = QA_PROMPT.format(
        design=state["code_design"]
    )

    response = llm.invoke(prompt)

    return {
        "test_cases": response.content
    }