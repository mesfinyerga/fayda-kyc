import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './auth/AuthContext';

const Home = () => <div className="p-8 text-center text-2xl">Welcome to Fayda KYC SaaS</div>;
const AdminDashboard = React.lazy(() => import('./dashboards/AdminDashboard'));
const ClientDashboard = React.lazy(() => import('./dashboards/ClientDashboard'));
const Login = React.lazy(() => import('./auth/Login'));

const App: React.FC = () => {
  return (
    <AuthProvider>
      <React.Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/admin/*" element={<AdminDashboard />} />
          <Route path="/client/*" element={<ClientDashboard />} />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </React.Suspense>
    </AuthProvider>
  );
};

export default App; 