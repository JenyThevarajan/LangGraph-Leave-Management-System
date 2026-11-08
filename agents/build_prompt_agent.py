# from llm import llm

# def build_prompt_agent(state):

#     prompt = f"""
#     You are a Senior Staff Engineer.

#     Requirements:
#     {state['requirements_doc']}

#     Architecture:
#     {state['architecture_doc']}

#     Design:
#     {state['code_design']}

#     Create a complete prompt for Cursor AI to generate the entire FastAPI project.

#     Return only the prompt.
#     """

#     response = llm.invoke(prompt)

#     return {
#         "build_prompt": response.content
#     }

from llm import llm
from prompts.build_prompt import BUILD_PROMPT

def build_prompt_agent(state):

    prompt = BUILD_PROMPT.format(
        requirements=state["requirements_doc"],
        architecture=state["architecture_doc"],
        design=state["code_design"]
    )

    response = llm.invoke(prompt)

    return {
        "build_prompt": response.content
    }