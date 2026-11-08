from typing import TypedDict

class SDLCState(TypedDict, total=False):

    user_requirement: str
    requirements_doc: str
    architecture_doc: str
    code_design: str
    review_report: str
    review_score: int
    test_cases: str
    build_prompt: str
    # source_code: str
    # deployment_files: str
    project_zip_path: str