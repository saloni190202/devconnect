# 🚀 GitHub Connector (FastAPI)

## 📌 Overview

This project is a **GitHub Cloud Connector** built using **FastAPI**.
It integrates with GitHub APIs using **OAuth 2.0 authentication** and provides endpoints to interact with repositories, issues, and pull requests.

The application also includes a **simple interactive frontend UI** served via FastAPI.

## ⚙️ Features

* 🔐 OAuth 2.0 Authentication (GitHub Login)
* 📦 Fetch User Repositories
* 🐞 List Issues from a Repository
* ➕ Create Issue in Repository
* 🔀 Create Pull Request (Bonus)
* 🌐 Interactive Frontend UI
* 🧱 Clean Architecture (Routes → Controllers → Services)


## 🛠️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/saloni190202/devconnect.git
cd backend


### 2. Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate      # Windows


### 3. Install Dependencies

pip install fastapi uvicorn python-dotenv requests


### 4. Setup Environment Variables

Create a `.env` file in root:


GITHUB_CLIENT_ID=your_client_id
GITHUB_CLIENT_SECRET=your_client_secret
GITHUB_REDIRECT_URI=http://127.0.0.1:8000/auth/callback
GITHUB_API_URL=https://api.github.com


### 5. Configure GitHub OAuth App

Go to:
https://github.com/settings/developers

Create OAuth App:

* **Homepage URL**

http://127.0.0.1:8000


* **Authorization Callback URL**

http://127.0.0.1:8000/auth/callback


## ▶️ How to Run the Project

Start the FastAPI server:

uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000


## 🔐 Authentication Flow

1. Click **Login**
2. Authenticate via GitHub
3. Copy the generated **Access Token**
4. Paste token into UI input field
5. Use API features

## 📡 API Endpoints

### 🔹 Authentication

* `GET /auth/login` → Redirect to GitHub OAuth
* `GET /auth/callback` → Returns access token UI


### 🔹 Repositories

* `GET /repos?token=YOUR_TOKEN`


### 🔹 Issues

* `GET /issues?token=YOUR_TOKEN&owner=OWNER&repo=REPO`


### 🔹 Create Issue

* `POST /create-issue`


Params:
token, owner, repo, title, body


### 🔹 Create Pull Request (Bonus)

* `POST /create-pull-request`

Params:
token, owner, repo, title, head, base, body (optional)


## 🎯 Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Auth:** OAuth 2.0 (GitHub)
* **API:** GitHub REST API


## ✅ Key Highlights

* Clean modular architecture
* Secure token handling using `.env`
* Real GitHub API integration
* Interactive UI for easy testing
* Bonus feature: Pull Request creation


## 📌 Notes

* Do not commit `.env` file
* Ensure correct OAuth credentials
* Token must have `repo` scope


## 🎉 Conclusion

This project demonstrates:

* API integration skills
* Authentication handling
* Clean backend architecture
* Full-stack implementation using FastAPI