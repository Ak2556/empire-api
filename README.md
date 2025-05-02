# 🏰 Empire API & Dashboard

[![CI](https://github.com/yourusername/empire-api/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/empire-api/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/yourusername/empire-api/badge.svg?branch=main)](https://coveralls.io/github/yourusername/empire-api?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Deploy Backend](https://img.shields.io/badge/Backend-Render-blue?logo=render)](https://render.com/)
[![Deploy Frontend](https://img.shields.io/badge/Frontend-Vercel-black?logo=vercel)](https://vercel.com/)

---

A modern, production-grade SaaS starter kit with a **FastAPI** backend (MongoDB, JWT Auth) and a **React + Material UI** frontend.  
Built for scalable, secure user management and rapid SaaS prototyping.

---

## 🚀 Features

- **User Signup & Login** with JWT authentication
- **MongoDB Atlas** async database integration (Motor)
- **React** frontend with Material UI, responsive dashboard, and sidebar navigation
- **Full-stack JWT Auth**: Secure, stateless sessions
- **CORS** enabled for frontend-backend communication
- **Robust CRUD** and error handling
- **Fully tested** backend (FastAPI TestClient, mongomock)
- **Production-ready** structure and best practices

---

## 🖥️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | FastAPI, Motor (MongoDB), JWT     |
| Frontend   | React (Vite), Material UI, Axios  |
| Auth       | JWT (PyJWT), localStorage (FE)    |
| Testing    | FastAPI TestClient, mongomock     |
| DevOps     | Python-dotenv, CORS, Vercel/Render-ready |

---

## 📦 Project Structure

```
empire-api/
├── app/                # FastAPI backend
│   ├── main.py         # API routes & app setup
│   ├── models.py       # Pydantic models
│   ├── crud.py         # DB operations
│   ├── database.py     # MongoDB connection
│   ├── security.py     # Password/JWT utils
│   └── test_main.py    # Backend tests
├── frontend/           # React frontend (Vite)
│   ├── src/pages/      # Home, Login, Signup, Dashboard, etc.
│   ├── src/assets/     # Images, styles
│   └── ...             # Components, theme, etc.
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment config
├── README.md           # This file
└── ...                 # venv, .gitignore, etc.
```

---

## ⚙️ Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/empire-api.git
cd empire-api
```

### 2. **Backend Setup (FastAPI)**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Copy `.env.example` to `.env` and fill in your MongoDB URI and secret key:

  ```
  MONGO_URI=mongodb+srv://<username>:<password>@<cluster-address>/<dbname>?retryWrites=true&w=majority
  SECRET_KEY=your_production_secret_key
  ```

- Start the backend server:

  ```bash
  uvicorn app.main:app --reload
  ```

- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

### 3. **Frontend Setup (React + Vite)**

```bash
cd frontend
npm install
npm run dev
```

- The frontend will run on [http://localhost:5173](http://localhost:5173) (default Vite port).

- Configure the frontend to point to your backend API (see `src/api.js` or similar).

---

## 🛡️ Environment Variables

Copy `.env.example` to `.env` and fill in:

```env
# Backend
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_jwt_secret_key

# (Frontend: if using .env for API URL)
VITE_API_URL=http://localhost:8000
```

---

## 🧪 Running Tests

- **Backend:**  
  ```bash
  pytest app/test_main.py
  ```
  (Uses mongomock for isolated DB tests.)

- **Frontend:**  
  Add and run tests with your preferred React testing library.

---

## 🚀 Deployment

- **Backend:** Deploy to [Render](https://render.com/), [Fly.io](https://fly.io/), or [Railway](https://railway.app/).
- **Frontend:** Deploy to [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/).

See deployment guides in the wiki or add your own.

---

## 📝 API Endpoints (Backend)

| Method | Route      | Description                        |
|--------|------------|------------------------------------|
| POST   | `/signup`  | Register new user (JWT returned)   |
| POST   | `/login`   | Login, receive JWT                 |
| GET    | `/get_users` | List all users (protected/admin) |
| GET    | `/`        | Health check                       |

See `/docs` for full OpenAPI schema.

---

## ✨ Future Enhancements

- Role-based authorization (admin/user)
- Social login (OAuth)
- Multi-tenant SaaS support
- CI/CD (GitHub Actions)
- Cloud deployment scripts

---

## 👑 Author

**Akash Thakur**  
Full Stack Developer | Backend Engineer | SaaS Enthusiast

---

## 🛡️ Security & Best Practices

- Passwords hashed (bcrypt) before storage
- JWT secrets and DB URIs never committed
- CORS and environment isolation enabled
- All secrets in `.env` (never commit this file!)

---

## 📄 License

MIT — see [LICENSE](./LICENSE)

---

**Ready to launch your SaaS? Fork, star, and build!**

---

### Badges (optional)

Add CI, coverage, or deployment badges here for extra polish.

---

**If you need a matching `.env.example` or want to add CI/CD, let me know!**
