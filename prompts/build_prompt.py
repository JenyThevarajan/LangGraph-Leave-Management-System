# BUILD_PROMPT = """
# You are a Staff Engineer.

# Based on the SDLC artifacts:

# Requirements:
# {requirements}

# Architecture:
# {architecture}

# Design:
# {design}

# Generate a Cursor AI prompt that can build the complete FastAPI application.

# Return ONLY the prompt.
# """
BUILD_PROMPT = """
Act as a Senior FastAPI Engineer.

Create a production-ready FastAPI application.

Business Requirements:
{requirements}

Architecture:
{architecture}

Design:
{design}

Generate:

1. Project Folder Structure
2. FastAPI Application
3. SQLAlchemy Models
4. Pydantic Schemas
5. Service Layer
6. Repository Layer
7. API Routes
8. Authentication
9. Dockerfile
10. requirements.txt

Output complete code with file names.

Return only the implementation.
"""