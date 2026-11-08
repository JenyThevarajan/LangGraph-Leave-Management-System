from llm import llm
from prompts.code_generator_prompt import CODE_GENERATOR_PROMPT

def code_generator(state):

    prompt = CODE_GENERATOR_PROMPT.format(
        requirements=state["requirements_doc"],
        architecture=state["architecture_doc"],
        design=state["code_design"]
    )

    response = llm.invoke(prompt)

    return {
        "source_code": response.content
    }