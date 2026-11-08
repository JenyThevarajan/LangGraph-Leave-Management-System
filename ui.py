# import streamlit as st
# import requests

# st.set_page_config(
#     page_title="Agentic SDLC",
#     layout="wide"
# )

# st.title("🚀 Agentic AI SDLC Assistant")

# requirement = st.text_area(
#     "Enter Business Requirement",
#     height=200,
#     placeholder="Build Leave Management System..."
# )

# if st.button("Generate SDLC"):

#     with st.spinner("Agents working..."):

#         response = requests.post(
#             "http://127.0.0.1:8000/generate",
#             json={
#                 "requirement": requirement
#             }
#         )

#     if response.status_code != 200:
#         st.error(response.text)
#         st.stop()

#     result = response.json()

#     tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
#         "Requirements",
#         "Architecture",
#         "Design",
#         "Review",
#         "Testing",
#         "Build Prompt",
#         # "Source Code",
#         # "Deployment"
#         "Project Download"
#     ])

#     with tab1:
#         #st.markdown(result["requirements"])
#         st.markdown(result.get("requirements", ""))

#     with tab2:
#         st.markdown(result.get("architecture", ""))

#     with tab3:
#         st.markdown(result.get("design", ""))

#     with tab4:
#         st.markdown(result.get("review", ""))

#     with tab5:
#         st.markdown(result.get("tests", ""))

#     with tab6:
#         st.code(
#             result.get("code_design", ""),
#             language="markdown"
#         )

#     # with tab7:
#     #     st.markdown(result.get("source_code",""))

#     # with tab8:
#     #     st.markdown(result.get("deployment_files",""))

#     # with tab7:
#     #     zip_path = result.get(
#     #         "project_zip_path"
#     #     )

#     #     if zip_path and os.path.exists(zip_path):

#     #         with open(zip_path, "rb") as file:

#     #             st.download_button(
#     #                 "Download Generated Project",
#     #                 file,
#     #                 file_name="generated_project.zip",
#     #                 mime="application/zip"
#     #             )
#     with tab7:

#         zip_path = result.get(
#             "project_zip_path"
#         )

#         if zip_path:

#             with open(zip_path, "rb") as file:

#                 st.download_button(
#                     label="Download Project ZIP",
#                     data=file,
#                     file_name="generated_project.zip",
#                     mime="application/zip"
#                 )

import os
import streamlit as st

st.set_page_config(page_title="Agentic SDLC", layout="wide")

# Make Streamlit secrets (API keys etc.) visible as environment variables
# BEFORE importing the graph, because the agents may create their LLM clients at import time.
try:
    for key in st.secrets:
        value = st.secrets[key]
        if isinstance(value, (str, int, float)):
            os.environ.setdefault(key, str(value))
except Exception:
    pass  # no secrets file when running locally; a .env file is used instead

from graph import graph

st.title("🚀 Agentic AI SDLC Assistant")

requirement = st.text_area(
    "Enter Business Requirement",
    height=200,
    placeholder="Build Leave Management System...",
)

if st.button("Generate SDLC"):
    if not requirement.strip():
        st.warning("Please enter a business requirement.")
        st.stop()

    with st.spinner("Agents working..."):
        try:
            state = graph.invoke({"user_requirement": requirement})
        except Exception as e:
            st.error(f"Generation failed: {e}")
            st.stop()

    zip_bytes = None
    zip_path = state.get("project_zip_path")
    if zip_path and os.path.exists(zip_path):
        with open(zip_path, "rb") as f:
            zip_bytes = f.read()

    # Keep results in session state so they survive Streamlit reruns
    # (clicking the download button reruns the script and would otherwise clear the tabs).
    st.session_state["result"] = {
        "requirements": state.get("requirements_doc", ""),
        "architecture": state.get("architecture_doc", ""),
        "design": state.get("code_design", ""),
        "review": state.get("review_report", ""),
        "tests": state.get("test_cases", ""),
        "code_design": state.get("code_design", ""),
        "zip_bytes": zip_bytes,
    }

result = st.session_state.get("result")

if result:
    tabs = st.tabs([
        "Requirements", "Architecture", "Design", "Review",
        "Testing", "Build Prompt", "Project Download",
    ])

    with tabs[0]:
        st.markdown(result["requirements"])
    with tabs[1]:
        st.markdown(result["architecture"])
    with tabs[2]:
        st.markdown(result["design"])
    with tabs[3]:
        st.markdown(result["review"])
    with tabs[4]:
        st.markdown(result["tests"])
    with tabs[5]:
        st.code(result["code_design"], language="markdown")
    with tabs[6]:
        if result["zip_bytes"]:
            st.download_button(
                label="Download Project ZIP",
                data=result["zip_bytes"],
                file_name="generated_project.zip",
                mime="application/zip",
            )
        else:
            st.info("No project ZIP was produced.")