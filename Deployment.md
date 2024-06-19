# Deployment Instructions for My Web App

## Overview
This web app is designed to support men's mental health by providing accessible and confidential therapy resources. The app aims to break the stigma around mental health issues and offer a safe space for men to seek help and support.
The goal of our app is to make mental health care more approachable and accessible for men, encouraging them to prioritize their mental well-being and seek help when needed.

## Prerequisites
- Render.com account

## Steps to Deploy on Render.com

### Step 1: Sign in to Render.com
Navigate to [Render.com](https://render.com) and sign in to your account.

### Step 2: Create a New Web Service
Go to the Render Dashboard and click on "New" then select "Web Service".

### Step 3: Connect Your Repository
Use my github.com/CaoimheWiggles/python-project to deploy onto Render

### Step 4: Configure the Web Service
- **Name:** python-project-1
- **Build Command:**  pip install -r requirements.txt
- **Start Command:** gunicorn app:app

### Step 5: Deploy the Web Service
Click on "Create Web Service" to deploy. Wait for the deployment process to complete.

## Accessing the Web App
Once the deployment is successful, access your web app at the provided URL: `https://python-project-1-q0uf.onrender.com/`.


