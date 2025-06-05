# Fayda KYC SaaS Backend

This is a production-ready, multi-tenant KYC SaaS backend based on Ethiopia's Fayda ID system. Built with Django REST Framework, PostgreSQL, and Docker, it follows industry best practices for security, scalability, and maintainability.

## Features
- Multi-tenant (organization-based) architecture
- Role-based authentication and permissions
- Fayda KYC verification engine
- Usage tracking, quota, and rate limiting
- Subscription and payment management (Stripe, Telebirr, Chapa)
- Audit logging and admin dashboard
- Secure REST API (JWT/session)
- Swagger/OpenAPI documentation
- Dockerized for local and production deployment

## Folder Structure
```
backend/
├── config/                  # Django project settings and URLs
├── core/                    # Users, organizations, roles, permissions
├── kyc/                     # KYC verification logic and endpoints
├── payments/                # Payment and subscription logic
├── audit/                   # Audit logging
├── notifications/           # Email/SMS/Slack notifications
├── webhooks/                # Webhook endpoints
├── tests/                   # Unit and integration tests
├── docs/                    # API documentation (Swagger/OpenAPI)
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Quick Start
1. Copy `.env.example` to `.env` and set environment variables.
2. Build and run with Docker Compose:
   ```sh
   docker-compose up --build
   ```
3. Access API at `http://localhost:8000/api/` and docs at `/api/docs/`.

## Best Practices
- All sensitive data is stored in environment variables.
- Passwords are hashed using Django's default hasher.
- JWT authentication is used for API endpoints.
- All endpoints are protected by role-based permissions and quota/rate limiting.
- Audit logs are recorded for all critical actions.

---

For detailed setup, see each app's README or docstrings in the codebase. 