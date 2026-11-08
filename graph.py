from langgraph.graph import StateGraph, END

from state import SDLCState

from agents.product_owner import product_owner
from agents.architect import architect
from agents.developer import developer
from agents.reviewer import reviewer
from agents.qa import qa
from agents.build_prompt_agent import build_prompt_agent
# from agents.code_generator import code_generator
#from agents.deployment import deployment
from agents.project_builder import project_builder

workflow = StateGraph(SDLCState)

# Nodes
workflow.add_node("po", product_owner)
workflow.add_node("architect", architect)
workflow.add_node("developer", developer)
workflow.add_node("reviewer", reviewer)
workflow.add_node("qa", qa)
workflow.add_node("build_prompt", build_prompt_agent)
# workflow.add_node("code_generator", code_generator)
# workflow.add_node("deployment", deployment)
workflow.add_node("project_builder", project_builder)

# Entry Point
workflow.set_entry_point("po")

# Main Flow
workflow.add_edge("po", "architect")
workflow.add_edge("architect", "developer")
workflow.add_edge("developer", "reviewer")


# Review Router
def review_router(state):

    score = state.get("review_score", 100)

    if score < 80:
        return "developer"

    return "qa"


workflow.add_conditional_edges(
    "reviewer",
    review_router
)

# Continue Flow
# workflow.add_edge("qa", "build_prompt")
# workflow.add_edge("build_prompt", "code_generator")
# workflow.add_edge("code_generator", "deployment")

# workflow.add_edge("deployment", "project_builder")
workflow.add_edge("qa", "build_prompt")

workflow.add_edge("build_prompt", "project_builder")

workflow.add_edge("project_builder", END)

graph = workflow.compile()