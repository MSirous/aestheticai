# 🎨 AestheticAI – Auth API

AestheticAI is a FastAPI-based backend project designed to support an AI-powered artistic platform. This repository includes a robust user authentication system with role-based access and verification flow – entirely command-line driven for minimal GUI distraction.

---

## 🌟 Features Implemented So Far

- ✅ User Registration (default role: `artist`)
- ✅ Secure Password Hashing with Bcrypt
- ✅ JWT-based Authentication System
- ✅ Account Verification via Verification Code
- ✅ Role-based Access (admin/artist/future roles)
- ✅ Token Authorization with FastAPI Dependency Injection
- ✅ Swagger & Postman Ready for Testing

---

## 🛠️ Tech Stack

- Python 3.10
- FastAPI
- SQLAlchemy (ORM)
- Alembic (Migrations)
- PostgreSQL
- Pydantic
- Bcrypt
- JWT (via `python-jose`)

---

## 📌 Installation & Setup (Terminal-Based)

```bash
# Clone the repo
git clone https://github.com/your-username/aestheticai.git
cd aestheticai/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create the PostgreSQL DB manually or via terminal
# Example: psql -U postgres -c 'CREATE DATABASE aestheticai;'

# Run Alembic migrations
alembic upgrade head

# Launch server
uvicorn app.main:app --reload

## 👩‍💻 Author  
Made with ❤️ by [Mahsa Sirous](mailto:mahsa.sirous@emu.edu.tr)
