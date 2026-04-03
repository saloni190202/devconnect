from fastapi import FastAPI
from routes.github_routes import router as github_router

app = FastAPI(title="GitHub Connector API")

app.include_router(github_router)


@app.get("/")
def root():
    return {"message": "GitHub Connector Running 🚀"}