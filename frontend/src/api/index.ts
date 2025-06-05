/// <reference types="vite/client" />
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/',
  withCredentials: true,
});

export const login = async (email: string, password: string) => {
  const response = await api.post('/auth/login/', { email, password });
  return response.data;
};

export const getCurrentUser = async (token: string) => {
  const response = await api.get('/users/me/', {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};

export default api; 