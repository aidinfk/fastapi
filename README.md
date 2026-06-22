# 🚀 Advanced FastAPI Backend with ML Integration

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791)
![License](https://img.shields.io/badge/license-MIT-green)

A production‑ready **FastAPI** backend that demonstrates modern async API design, secure authentication, background processing, and seamless integration of a machine learning model – all backed by a robust PostgreSQL database with Alembic migrations.

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Core Implementation Details](#-core-implementation-details)
  - [1. Application Setup](#1-application-setup)
  - [2. Path & Query Parameters](#2-path--query-parameters)
  - [3. Request Body](#3-request-body)
  - [4. Response Model](#4-response-model)
  - [5. Templates](#5-templates)
  - [6. SQLModel + PostgreSQL](#6-sqlmodel--postgresql)
  - [7. Alembic Migrations](#7-alembic-migrations)
  - [8. Modular Routers](#8-modular-routers)
  - [9. Update & Delete Operations](#9-update--delete-operations)
  - [10. Async/Await](#10-asyncawait)
  - [11. Passlib Password Hashing](#11-passlib-password-hashing)
  - [12. Middleware](#12-middleware)
  - [13. Events (Startup/Shutdown)](#13-events-startupshutdown)
  - [14. Database Relationships & Back‑populate](#14-database-relationships--back-populate)
  - [15. JWT Authentication](#15-jwt-authentication)
  - [16. Get Current User](#16-get-current-user)
  - [17. SMTP Email Sending](#17-smtp-email-sending)
  - [18. Background Tasks](#18-background-tasks)
  - [19. scikit‑learn Integration](#19-scikit-learn-integration)
  - [20. Authorization & Roles](#20-authorization--roles)
- [Environment Variables](#-environment-variables)
- [License](#-license)

---

## ✨ Features

- **Full Async CRUD** with PostgreSQL and SQLModel
- **JWT Authentication** with role‑based authorization
- **User Management** – registration, login, and current‑user retrieval
- **Email Verification** via SMTP using background tasks
- **Password Hashing** with Passlib
- **Database Migrations** managed by Alembic
- **Request Validation** using Pydantic models (body, path, query)
- **Response Serialization** with FastAPI response models
- **Jinja2 Template Rendering** for server‑side views
- **Custom Middleware** for logging, CORS, and request processing
- **Application Events** to handle database connection pools
- **SQLModel Relationships** with back‑population
- **Machine Learning** endpoint serving a trained scikit‑learn model
- **Clean, scalable project structure** using APIRouters

---

## 🧰 Tech Stack

| Layer           | Technology                          |
|-----------------|-------------------------------------|
| Framework       | FastAPI (async)                     |
| ORM             | SQLModel (SQLAlchemy 2.0)           |
| Database        | PostgreSQL + asyncpg                |
| Migrations      | Alembic                             |
| Authentication  | PyJWT, Passlib              |
| Templating      | Jinja2                              |
| Email           | fastapi‑mail           |
| ML              | scikit‑learn, joblib                |
| Async          | async/await, BackgroundTasks        |
| Validation      | Pydantic v2                         |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL running locally or via Docker
- `pip` / `virtualenv`

### Installation

```bash
git clone https://github.com/aidinfk/fastapi.git
cd fastapi
python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # Fill in your credentials
alembic upgrade head
python main.py

The API is now available at http://localhost:8000
Interactive docs: http://localhost:8000/docs
