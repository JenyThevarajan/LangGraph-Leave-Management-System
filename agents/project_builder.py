# import os
# import zipfile

# def project_builder(state):

#     project_name = "generated_project"

#     os.makedirs(project_name, exist_ok=True)

#     backend_dir = os.path.join(project_name, "backend")

#     os.makedirs(backend_dir, exist_ok=True)

#     with open(
#         os.path.join(backend_dir, "generated_code.md"),
#         "w",
#         encoding="utf-8"
#     ) as f:

#         f.write(state.get("source_code", ""))

#     with open(
#         os.path.join(project_name, "deployment.md"),
#         "w",
#         encoding="utf-8"
#     ) as f:

#         f.write(state.get("deployment_files", ""))

#     zip_name = f"{project_name}.zip"

#     with zipfile.ZipFile(
#         zip_name,
#         "w",
#         zipfile.ZIP_DEFLATED
#     ) as zipf:

#         for root, dirs, files in os.walk(project_name):

#             for file in files:

#                 path = os.path.join(root, file)

#                 zipf.write(
#                     path,
#                     os.path.relpath(path, project_name)
#                 )

#     return {
#         "project_zip_path": zip_name
#     }

import os
import zipfile


def project_builder(state):

    project_name = "generated_project"

    backend_dir = os.path.join(project_name, "backend")

    os.makedirs(backend_dir, exist_ok=True)

    # main.py

    main_py = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}
"""

    with open(
        os.path.join(backend_dir, "main.py"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(main_py)

    # requirements.txt

    requirements_txt = """
fastapi
uvicorn
"""

    with open(
        os.path.join(project_name, "requirements.txt"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(requirements_txt)

    # Dockerfile

    dockerfile = """
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

    with open(
        os.path.join(project_name, "Dockerfile"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(dockerfile)

    # README

    readme = f"""
# Generated Project

Requirement:

{state.get("user_requirement", "")}

Build Prompt:

{state.get("build_prompt", "")}
"""

    with open(
        os.path.join(project_name, "README.md"),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(readme)

    zip_path = "generated_project.zip"

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for root, dirs, files in os.walk(project_name):

            for file in files:

                full_path = os.path.join(root, file)

                zipf.write(
                    full_path,
                    os.path.relpath(
                        full_path,
                        project_name
                    )
                )

    return {
        "project_zip_path": zip_path
    }