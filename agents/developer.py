from llm import llm
from prompts.developer_prompt import DEVELOPER_PROMPT

def developer(state):

    prompt = DEVELOPER_PROMPT.format(
        architecture=state["architecture_doc"]
    )

    response = llm.invoke(prompt)
    print("Running Developer Agent")

    return {
        "code_design": response.content
    }