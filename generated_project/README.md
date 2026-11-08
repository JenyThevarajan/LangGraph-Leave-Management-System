
# Generated Project

Requirement:

Vibe code inventory management web application for AI & Data.

Build Prompt:

**Project Folder Structure**  

```
inventory-service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   ├── exceptions.py
│   │   └── logger.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── permission.py
│   │   ├── item.py
│   │   ├── item_version.py
│   │   ├── tag.py
│   │   ├── license.py
│   │   ├── comment.py
│   │   └── audit.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── item.py
│   │   ├── item_version.py
│   │   ├── tag.py
│   │   ├── license.py
│   │   ├── comment.py
│   │   └── notification.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── inventory_service.py
│   │   ├── search_service.py
│   │   ├── notification_service.py
│   │   └── audit_service.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── user_repo.py
│   │   ├── item_repo.py
│   │   ├── tag_repo.py
│   │   ├── license_repo.py
│   │   ├── comment_repo.py
│   │   └── audit_repo.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── items.py
│   │   ├── tags.py
│   │   ├── licenses.py
│   │   ├── comments.py
│   │   ├── search.py
│   │   └── notifications.py
│   └── tests/
│       └── __init__.py
├── alembic/
│   └── (migration files – omitted for brevity)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

### 1. `app/main.py`

```python
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, items, tags, licenses, comments, search, notifications
from app.core.exceptions import HTTPException as CustomHTTPException
from app.core.logger import logger

app = FastAPI(
    title="Vibe Code Inventory Service",
    description="REST API for managing code snippets, datasets, and models.",
    version="1.0.0",
)

# CORS – adjust origins for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(tags.router, prefix="/tags", tags=["tags"])
app.include_router(licenses.router, prefix="/licenses", tags=["licenses"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(search.router, prefix="/search", tags=["search"])
app.include_router(notifications.router, prefix="/notifications", tags=["notifications"])

# Global exception handler
@app.exception_handler(CustomHTTPException)
async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
    logger.error(f"HTTP error: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

# Health check
@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}
```

---

### 2. `app/config.py`

```python
from pydantic import BaseSettings, Field
from typing import List, Optional

class Settings(BaseSettings):
    # General
    APP_NAME: str = "Vibe Inventory Service"
    ENV: str = Field("development", env="ENV")

    # Database
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # JWT
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: List[str] = ["*"]

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

---

### 3. `app/dependencies.py`

```python
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.config import settings
from sqlalchemy.orm import DeclarativeBase

# Async engine
engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)

# Session factory
async_session = async_sessionmaker(engine, expire_on_commit=False)

@asynccontextmanager
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
```

---

### 4. `app/core/security.py`

```python
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Dict, Any
from app.config import settings
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings
