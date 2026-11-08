from llm import llm
from prompts.architect_prompt import ARCHITECT_PROMPT

def architect(state):

    prompt = ARCHITECT_PROMPT.format(
        requirements=state["requirements_doc"]
    )

    response = llm.invoke(prompt)
    print("Running Architect Agent")

    return {
        "architecture_doc": response.content
    }