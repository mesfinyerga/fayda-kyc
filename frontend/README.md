# Fayda KYC SaaS Frontend

This is the frontend for the Fayda KYC SaaS platform, built with React and Tailwind CSS. It provides:

- Admin dashboard (user/client management, stats, billing, KYC logs)
- Client dashboard (KYC usage, team management, verification history, branding)
- Secure authentication (JWT/session)
- Responsive, professional UI
- API integration with the Django backend

## Stack
- React (with TypeScript)
- Tailwind CSS
- React Router
- State management (Context API or Redux)
- Axios for API calls

## Folder Structure
```
frontend/
├── public/
├── src/
│   ├── api/                # API service layer
│   ├── auth/               # Auth context, hooks
│   ├── components/         # Reusable UI components
│   ├── dashboards/
│   │   ├── AdminDashboard/
│   │   └── ClientDashboard/
│   ├── pages/              # Route-based pages
│   ├── styles/             # Tailwind config, global styles
│   ├── utils/              # Helpers
│   ├── App.tsx
│   ├── index.tsx
│   └── ...
├── tailwind.config.js
├── package.json
└── ...
```

## Quick Start
1. Install dependencies: `npm install`
2. Start dev server: `npm start`
3. Configure API URL in `.env`

---

See code and docs in each folder for details. 