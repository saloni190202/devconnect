from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from config import GITHUB_CLIENT_ID, GITHUB_REDIRECT_URI
from controllers.github_controller import GitHubController

router = APIRouter()


@router.get("/auth/login")
def github_login():
    url = (
        f"https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        f"&redirect_uri={GITHUB_REDIRECT_URI}"
        f"&scope=repo"
    )
    return RedirectResponse(url)


@router.get("/auth/callback")
def github_callback(code: str):
    token = GitHubController.exchange_code_for_token(code)
    return {"access_token": token}


@router.get("/repos")
def get_repos(token: str = Query(...)):
    return GitHubController.get_repositories(token)


@router.get("/issues")
def get_issues(token: str, owner: str, repo: str):
    return GitHubController.get_issues(token, owner, repo)


@router.post("/create-issue")
def create_issue(token: str, owner: str, repo: str, title: str, body: str):
    return GitHubController.create_issue(token, owner, repo, title, body)

@router.post("/create-pull-request")
def create_pull_request(
    token: str,
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: str = None
):
    return GitHubController.create_pull_request(
        token, owner, repo, title, head, base, body
    )