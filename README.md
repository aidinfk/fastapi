# 🚀 Advanced FastAPI Backend with ML Integration

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791)
![License](https://img.shields.io/badge/license-MIT-green)

A production‑ready **FastAPI** backend that demonstrates modern async API design, secure authentication, background processing, and seamless integration of a machine learning model – all backed by a robust PostgreSQL database with Alembic migrations.

---

1. Application Setup
Creating the main FastAPI instance, configuring metadata (title, version, docs), and registering routers, middleware, and lifecycle event handlers.

2. Path & Query Parameters
Values extracted from the URL – path parameters (e.g., /items/{id}) and query strings (e.g., ?search=term). FastAPI validates them using Path and Query.

3. Request Body
The JSON payload sent by the client in POST/PUT/PATCH requests, validated and parsed automatically using Pydantic models.

4. Response Model
A Pydantic model that filters and serializes the endpoint’s output. It ensures the API only returns intended fields and generates accurate OpenAPI documentation.

5. Templates
Using Jinja2 to render HTML on the server, useful for building simple web pages, email bodies, or admin panels directly from the backend.

6. SQLModel + PostgreSQL
An ORM that combines SQLAlchemy and Pydantic, allowing you to define database tables as Python classes and interact with PostgreSQL using an asynchronous driver (e.g., asyncpg).

7. Alembic Migrations
A tool for version-controlling database schema changes. Each migration is a script that applies or reverts changes (add tables, columns, etc.) in a reproducible way.

8. Modular Routers
Breaking the API into separate APIRouter instances grouped by feature (users, auth, etc.), then including them in the main app with prefixes and tags for better organization.

9. Update & Delete Operations
Implementing full CRUD: PUT/PATCH endpoints for updating records and DELETE for removing them, with proper validation and status codes.

10. Async/Await
Non-blocking I/O using Python’s async and await. Allows the server to handle many concurrent requests efficiently while waiting for database queries, external APIs, etc.

11. Passlib Password Hashing
Hashing user passwords with strong algorithms like bcrypt via Passlib. Passwords are never stored in plain text, and verification uses constant-time comparison to prevent timing attacks.

12. Middleware
A layer that intercepts every request/response. Common uses include logging, CORS headers, adding process-time headers, and early security checks.

13. Events (Startup/Shutdown)
Functions that run when the server starts (e.g., connect to database, load models) and stops (e.g., close connections, clean up). Managed via the lifespan context or @app.on_event decorators.

14. Database Relationships & Back-populate
Defining foreign key links between tables and using back_populates to create bidirectional references so that related objects can be accessed from either side (e.g., user.posts and post.user).

15. JWT Authentication
A stateless authentication method where a signed token (JWT) containing user info is issued after login. The client sends it in the Authorization header; the server validates the signature and expiry.

16. Get Current User
A reusable dependency that extracts the JWT from a request, decodes it, fetches the corresponding user from the database, and injects it into protected endpoints, returning 401 if invalid.

17. SMTP Email Sending
Sending transactional emails (verification, password reset) by connecting to an SMTP server. Often done asynchronously to avoid blocking the request cycle.

18. Background Tasks
Offloading slow operations (like sending an email) to run after the response is returned, using FastAPI’s BackgroundTasks, so the API remains responsive.

19. scikit-learn Integration
Loading a pre-trained machine learning model (saved with joblib or pickle) at startup and serving predictions through a dedicated API endpoint.

20. Authorization & Roles
Restricting access to certain endpoints based on user roles (e.g., admin vs. regular user). Typically implemented as a dependency that checks the role and raises a 403 Forbidden if insufficient.

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
