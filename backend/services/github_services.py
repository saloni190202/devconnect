import requests
from config import GITHUB_API_URL

class GitHubService:

    @staticmethod
    def get_access_token(code, client_id, client_secret):
        url = "https://github.com/login/oauth/access_token"

        headers = {"Accept": "application/json"}

        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code != 200:
            raise Exception("Failed to get access token")

        return response.json().get("access_token")


    @staticmethod
    def get_user_repos(token):
        url = f"{GITHUB_API_URL}/user/repos"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception("Failed to fetch repositories")

        return response.json()


    @staticmethod
    def list_issues(token, owner, repo):
        url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception("Failed to fetch issues")

        return response.json()


    @staticmethod
    def create_issue(token, owner, repo, title, body):
        url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        data = {
            "title": title,
            "body": body
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code not in [200, 201]:
            raise Exception("Failed to create issue")

        return response.json()
    
    @staticmethod
    def create_pull_request(token, owner, repo, title, head, base, body=None):
        url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        data = {
            "title": title,
            "head": head,   
            "base": base,   
            "body": body
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code not in [200, 201]:
            raise Exception(f"Failed to create pull request: {response.text}")

        return response.json()