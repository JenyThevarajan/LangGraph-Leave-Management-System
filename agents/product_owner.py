from llm import llm
from prompts.product_owner_prompt import PRODUCT_OWNER_PROMPT

def product_owner(state):

    prompt = PRODUCT_OWNER_PROMPT.format(
        requirement=state["user_requirement"]
    )

    response = llm.invoke(prompt)
    print("Running Product Owner Agent")

    return {
        "requirements_doc": response.content
    }