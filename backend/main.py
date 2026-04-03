from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes.github_routes import router as github_router
import os

app = FastAPI(title="GitHub Connector API")

# Include API routes
app.include_router(github_router)

# Serve static files (JS, CSS)
app.mount("/static", StaticFiles(directory="frontend"), name="static")


# Serve HTML
@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join("frontend", "index.html"))