# from fastapi import FastAPI

# from graph import graph

# app = FastAPI()


# @app.post("/generate")
# def generate(req: dict):

#     result = graph.invoke(
#         {
#             "user_requirement": req["requirement"]
#         }
#     )

#     return result
from fastapi import FastAPI
from graph import graph

app = FastAPI()


@app.get("/")
def health():
    return {
        "message": "Agentic SDLC Running"
    }


# @app.post("/generate")
# def generate(req: dict):

#     result = graph.invoke(
#         {
#             "user_requirement": req["requirement"]
#         }
#     )

#     return result

@app.post("/generate")
def generate(req: dict):

    result = graph.invoke({
        "user_requirement": req["requirement"]
    })

    return {
        "requirements": result["requirements_doc"],
        "architecture": result["architecture_doc"],
        "design": result["code_design"],
        "review": result["review_report"],
        "tests": result["test_cases"],
        "code_design": result["code_design"],
        # "source_code": result["source_code"],
        # "deployment_files": result["deployment_files"],
        "project_zip_path": result["project_zip_path"]
    }