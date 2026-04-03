from fastapi import HTTPException
from config import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET
from services.github_services import GitHubService


class GitHubController:

    @staticmethod
    def exchange_code_for_token(code: str):
        try:
            return GitHubService.get_access_token(
                code,
                GITHUB_CLIENT_ID,
                GITHUB_CLIENT_SECRET
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def get_repositories(token: str):
        try:
            return GitHubService.get_user_repos(token)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def get_issues(token: str, owner: str, repo: str):
        try:
            return GitHubService.list_issues(token, owner, repo)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def create_issue(token, owner, repo, title, body):
        try:
            return GitHubService.create_issue(token, owner, repo, title, body)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    @staticmethod
    def create_pull_request(token, owner, repo, title, head, base, body=None):
        try:
            return GitHubService.create_pull_request(
                token, owner, repo, title, head, base, body
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))