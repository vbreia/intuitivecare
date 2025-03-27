import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // URL do backend
});

// Interceptor para registrar as solicitações
api.interceptors.request.use((config) => {
  console.log("Enviando solicitação para:", config.baseURL + config.url);
  console.log("Configuração da solicitação:", config);
  return config;
});

export default api;