# Fayda KYC SaaS Platform

A world-class, multi-tenant KYC SaaS platform for Ethiopia and Africa, built with Django, React, PostgreSQL, and Docker.

---

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Environment Variables](#environment-variables)
- [Quick Start (Development)](#quick-start-development)
- [Production Deployment](#production-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Security Best Practices](#security-best-practices)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)

---

## Features
- Multi-tenant (organization-based) user management
- Role-based permissions (admin, verifier, viewer)
- Fayda ID KYC verification engine
- Usage tracking, quota, and rate limiting
- Subscription and payment management (Stripe, Chapa, Telebirr)
- Audit logging and admin dashboard
- Secure REST API (JWT)
- Swagger/OpenAPI docs
- Dockerized for local and production deployment
- CI/CD with GitHub Actions

---

## Architecture
- **Backend:** Django REST Framework, PostgreSQL, Celery (optional for async tasks)
- **Frontend:** React (TypeScript), Tailwind CSS, React Router
- **Payments:** Stripe (global), Chapa/Telebirr (Ethiopia)
- **Deployment:** Docker Compose, Nginx, GitHub Actions
- **Multi-tenancy:** Organization-based data isolation
- **Security:** JWT, rate limiting, audit logging, environment-based secrets

---

## Tech Stack
- **Backend:** Python 3.11, Django 4.x, DRF, PostgreSQL, Gunicorn
- **Frontend:** React 18, TypeScript, Tailwind CSS, Vite
- **Payments:** Stripe, Chapa, Telebirr (starter)
- **DevOps:** Docker, Docker Compose, Nginx, GitHub Actions

---

## Folder Structure
```
├── backend/         # Django backend (multi-tenant, DRF, PostgreSQL)
│   ├── core/        # Users, organizations, roles, permissions
│   ├── kyc/         # KYC verification logic
│   ├── payments/    # Payment and subscription logic
│   ├── audit/       # Audit logging
│   ├── ...
│   ├── config/      # Django settings, URLs, WSGI/ASGI
│   ├── requirements.txt
│   └── ...
├── frontend/        # React + Tailwind frontend
│   ├── src/
│   │   ├── api/     # API service layer
│   │   ├── auth/    # Auth context, hooks
│   │   ├── dashboards/
│   │   ├── ...
│   ├── package.json
│   └── ...
├── nginx/           # Nginx config for production
├── .github/workflows/ci-cd.yml # CI/CD pipeline
├── docker-compose.yml
├── README.md
└── ...
```

---

## Environment Variables
- **Backend:** See `backend/.env.example` for all required variables (Django, DB, Stripe, Chapa, Telebirr, email, etc.)
- **Frontend:** See `frontend/.env.example` (e.g., `VITE_API_URL`)
- **Never commit real secrets to version control!**

---

## Quick Start (Development)
1. Clone the repo and copy `.env.example` to `.env` in the project root, `backend/`, and `frontend/`.
2. Start the stack:
   ```sh
   docker-compose up --build
   ```
3. Access:
   - API: http://localhost:8000/api/
   - Frontend: http://localhost/
   - Swagger docs: http://localhost/api/docs/

---

## Production Deployment
- Use the provided `docker-compose.yml` and `nginx/nginx.conf` for production.
- Set all secrets in `.env` files (never commit real secrets).
- Use Railway, Render, AWS, or your preferred cloud for deployment.
- Nginx serves frontend, proxies API, and serves static/media files.
- For HTTPS, add SSL config to Nginx or use a cloud provider's SSL termination.

---

## CI/CD Pipeline
- GitHub Actions workflow in `.github/workflows/ci-cd.yml` for build, test, and deploy.
- Runs backend tests (pytest), builds frontend, and is ready for cloud deployment.
- Add your deployment provider's steps (Railway, Render, AWS, etc.).

---

## Security Best Practices
- All secrets in environment variables
- HTTPS enforced in production
- JWT for API authentication
- Rate limiting and quota enforcement
- Audit logging for compliance
- Regular dependency updates and security scans

---

## Documentation
- **API Docs:** `/api/docs/` (Swagger/OpenAPI)
- **Backend:** `backend/README.md`
- **Frontend:** `frontend/README.md`
- **.env Setup:** See `.env.example` in each app

---

## Troubleshooting
- **Docker build fails:** Check `.env` files and Docker logs for missing variables or build errors.
- **Frontend not loading:** Ensure `VITE_API_URL` is set correctly and backend is running.
- **Database issues:** Ensure Postgres service is healthy and credentials match `.env`.
- **CI/CD failures:** Check GitHub Actions logs for details.

---

**For questions or contributions, open an issue or pull request.** 

Run:
```sh
docker-compose build  # run from the project root
```
