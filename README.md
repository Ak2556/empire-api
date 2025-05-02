# 🏰 Empire API & Dashboard

[![CI](https://github.com/Ak2556/empire-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Ak2556/empire-api/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/Ak2556/empire-api/badge.svg?branch=main)](https://coveralls.io/github/Ak2556/empire-api?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Deploy Backend](https://img.shields.io/badge/Backend-Render-blue?logo=render)](https://render.com/)
[![Deploy Frontend](https://img.shields.io/badge/Frontend-Vercel-black?logo=vercel)](https://vercel.com/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-green?logo=vercel)](https://empire-api-frontend.vercel.app/)

## Overview

**Empire API** is a modern, production-ready SaaS starter kit featuring a FastAPI backend and a React-based dashboard. Designed for developers building scalable, secure applications with rapid prototyping in mind, it includes user authentication, database integration, and a clean, responsive UI. See architecture diagram below for high-level structure.

## Architecture Diagram

![Empire API Architecture](https://user-images.githubusercontent.com/yourusername/empire-api-architecture.png)

## Features

- JWT-based signup & login  
- MongoDB Atlas (via Motor)  
- Material UI-powered dashboard with Vite  
- Robust FastAPI backend (fully tested)  
- Role-ready architecture for future multi-tenant support  
- Production-optimized deployment setup  

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | FastAPI, Motor (MongoDB), JWT     |
| Frontend   | React (Vite), Material UI, Axios  |
| Auth       | PyJWT, localStorage               |
| Testing    | FastAPI TestClient, mongomock     |
| DevOps     | Python-dotenv, CORS, Vercel, Render |

## Project Structure

```
empire-api/
├── app/             → FastAPI backend
├── frontend/        → React frontend (Vite)
├── .env.example     → Example environment variables
├── requirements.txt → Python dependencies
└── README.md        → This file
```

## Getting Started

```bash
# Clone
git clone https://github.com/Ak2556/empire-api.git && cd empire-api

# Backend Setup
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Edit with Mongo URI & secret
uvicorn app.main:app --reload

# Frontend Setup
cd frontend
npm install
npm run dev
```

## Testing

```bash
pytest app/test_main.py  # Backend tests with mongomock
```

## API Endpoints

| Method | Route         | Description                  |
|--------|---------------|------------------------------|
| POST   | /signup       | Create a new user            |
| POST   | /login        | User login, receive JWT      |
| GET    | /get_users    | Admin-only user listing      |
| GET    | /             | Health check                 |

Full docs available at `/docs`.

## Deployment

Deploy backend to **Render**, frontend to **Vercel** or **Netlify**. Environment variables are required on both sides. Refer to `.env.example` for structure.

## Author

**Akash Thakur**  
Full Stack Developer | Backend Engineer | SaaS Enthusiast

## License

MIT © Akash Thakur — see [LICENSE](./LICENSE)
