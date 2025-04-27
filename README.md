# Empire API 🛡️

A production-grade backend API for secure user management, built using **FastAPI** and **MongoDB Atlas**.  
Designed to serve as the authentication and user base for future AI SaaS platforms and scalable cloud applications.

---

## 🚀 Features

- User Signup with secure password hashing (bcrypt encryption)
- Fetch all users (admin-level endpoint)
- MongoDB Atlas cloud database integration
- Environment variable management via `.env`
- Modular professional project structure
- Async support for high performance
- Fully tested with Swagger UI API docs

---

## ⚙️ Tech Stack

| Layer | Technology |
|:---|:---|
| Backend Framework | FastAPI |
| Database | MongoDB Atlas (Motor async driver) |
| Password Security | bcrypt (passlib) |
| Environment Variables | python-dotenv |
| API Documentation | Swagger UI (`/docs`) |
| Hosting Ready | Render / Railway / Vercel (future deployment) |

---

## 📜 API Endpoints

| Method | Route | Description |
|:---|:---|:---|
| `POST` | `/signup` | Create a new user securely (hashed password) |
| `POST` | `/create_user` | Create a basic user (non-encrypted, testing only) |
| `GET` | `/get_users` | Retrieve all registered users |
| `GET` | `/` | Check if server is live |

---

## 🛠️ Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/Ak2556/empire_api.git
cd empire_api
```

2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Setup Environment Variables

Create a `.env` file based on `.env.example`:

```plaintext
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-address>/<dbname>?retryWrites=true&w=majority&appName=<yourAppName>
```

5. Run the Server Locally

```bash
uvicorn app.main:app --reload
```

6. Test the API

Visit:

```plaintext
http://127.0.0.1:8000/docs
```
✅ Test all routes directly via Swagger UI!

---

## 📦 Project Structure

```plaintext
empire_api/
├── app/
│   ├── crud.py          # Database operations (Create, Read)
│   ├── database.py      # MongoDB connection setup
│   ├── main.py          # API route definitions
│   ├── models.py        # Data models and validation
│   ├── security.py      # Password hashing and verification
├── .env                 # Environment variables (private, not pushed)
├── .env.example         # Example env file for GitHub
├── README.md            # Project documentation
├── requirements.txt     # Project dependencies
└── venv/                # Virtual environment folder (not pushed)
```

---

## 🛡️ Security Features

- All passwords are hashed using bcrypt before saving to database.
- Environment secrets are loaded safely through `.env`.
- Sensitive information is excluded from GitHub commits.

---

## ✨ Future Enhancements

- Implement JWT authentication for login and secure protected routes
- Role-based user authorization (admin, user)
- OpenAI API integration for AI-powered services
- Full SaaS user dashboard development

---

# 👑 Built By: **Akash Thakur**  
> Full Stack Developer | Backend Engineer | Future SaaS Founder
