from llm import llm
from prompts.deployment_prompt import DEPLOYMENT_PROMPT

def deployment(state):

    prompt = DEPLOYMENT_PROMPT.format(
        design=state["code_design"]
    )

    response = llm.invoke(prompt)

    return {
        "deployment_files": response.content
    }