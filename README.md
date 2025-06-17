# Flask App Deployment with CI/CD on Google Cloud Run

This project shows how to create, containerize, and deploy a simple Flask API to Google Cloud Run using GitHub Actions for automated deployment.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Run Locally](#run-locally)
- [Run with Docker](#run-with-docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [Required GitHub Secrets](#required-github-secrets)
- [Cloud Run Endpoint](#cloud-run-endpoint)

---

## Overview

This project contains a Flask app with a `/tasks` endpoint. The app is containerized using Docker and deployed to Google Cloud Run automatically with GitHub Actions when changes are made to the `master` branch.

---

## Features

- A simple REST API with `GET /tasks`
- Auto-deployment to Google Cloud Run
- CI/CD pipeline with GitHub Actions
- Docker containerization
- Securely stores credentials using GitHub Secrets

---

## Tech Stack

- **Flask** — Web framework (Python)
- **Docker** — Containerization
- **GitHub Actions** — Automates deployment
- **Google Cloud Run** — Cloud hosting
- **GitHub Secrets** — Secure credentials

---

## Project Structure

```plaintext
flask-cloudrun-cicd/
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Actions workflow
├── app.py                    # Flask app
├── Dockerfile                # Docker build instructions
├── docker-compose.yml        # Optional for local dev
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

---

## How It Works

1. Code is pushed to `master` on GitHub.
2. GitHub Actions builds a Docker image from the Flask app.
3. The image is pushed to Google Artifact Registry.
4. Google Cloud Run pulls the image and deploys it.
5. The app is available via a Cloud Run URL.

---

## Run Locally

To run the Flask app locally:

```bash
git clone https://github.com/your-username/flask-cloudrun-cicd.git
cd flask-cloudrun-cicd
pip install -r requirements.txt
python app.py
```

Visit: [http://localhost:8080/tasks](http://localhost:8080/tasks)

---

## Run with Docker

To run with Docker:

```bash
docker build -t flask-cloudrun-cicd .
docker run -p 8080:8080 flask-cloudrun-cicd
```

---

## CI/CD Pipeline

The GitHub Actions workflow in `.github/workflows/deploy.yml`:

1. Authenticates with Google Cloud
2. Builds and pushes the Docker image
3. Deploys the image to Google Cloud Run

---

## Required GitHub Secrets

Set up these secrets in your GitHub repo:

- `GCP_CREDENTIALS` — Base64-encoded Google Cloud service account key
- `GCP_PROJECT_ID` — Your Google Cloud project ID
- `GCP_REGION` — Deployment region (e.g., `asia-southeast2`)

---

## Cloud Run Endpoint

Once deployed, the app will be available at:

```http
GET https://<your-cloud-run-url>/tasks
```

---

Thank you for reading!
