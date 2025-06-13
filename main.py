from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes
from app.db.database import Base, get_engine_and_session

def create_app():
    """Create and configure the FastAPI application."""

    app = FastAPI(
        title="RPN Calculator API",
        description="REST API to evaluate expressions in Reverse Polish Notation (RPN).",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    engine, _ = get_engine_and_session()
    Base.metadata.create_all(bind=engine)
    app.include_router(routes.router)

    return app

app = create_app()
