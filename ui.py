import streamlit as st
import requests

st.set_page_config(
    page_title="Agentic SDLC",
    layout="wide"
)

st.title("🚀 Agentic AI SDLC Assistant")

requirement = st.text_area(
    "Enter Business Requirement",
    height=200,
    placeholder="Build Leave Management System..."
)

if st.button("Generate SDLC"):

    with st.spinner("Agents working..."):

        response = requests.post(
            "http://127.0.0.1:8000/generate",
            json={
                "requirement": requirement
            }
        )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    result = response.json()

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Requirements",
        "Architecture",
        "Design",
        "Review",
        "Testing",
        "Build Prompt",
        # "Source Code",
        # "Deployment"
        "Project Download"
    ])

    with tab1:
        #st.markdown(result["requirements"])
        st.markdown(result.get("requirements", ""))

    with tab2:
        st.markdown(result.get("architecture", ""))

    with tab3:
        st.markdown(result.get("design", ""))

    with tab4:
        st.markdown(result.get("review", ""))

    with tab5:
        st.markdown(result.get("tests", ""))

    with tab6:
        st.code(
            result.get("code_design", ""),
            language="markdown"
        )

    # with tab7:
    #     st.markdown(result.get("source_code",""))

    # with tab8:
    #     st.markdown(result.get("deployment_files",""))

    # with tab7:
    #     zip_path = result.get(
    #         "project_zip_path"
    #     )

    #     if zip_path and os.path.exists(zip_path):

    #         with open(zip_path, "rb") as file:

    #             st.download_button(
    #                 "Download Generated Project",
    #                 file,
    #                 file_name="generated_project.zip",
    #                 mime="application/zip"
    #             )
    with tab7:

        zip_path = result.get(
            "project_zip_path"
        )

        if zip_path:

            with open(zip_path, "rb") as file:

                st.download_button(
                    label="Download Project ZIP",
                    data=file,
                    file_name="generated_project.zip",
                    mime="application/zip"
                )
