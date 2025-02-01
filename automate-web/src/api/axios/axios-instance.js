import axios from 'axios';

// Instância do Axios configurada
const api = axios.create({
    baseURL: 'http://127.0.0.1:5000', // URL base da API
    timeout: 10000, // Timeout de 1 segundo
    headers: {
        'Content-Type': 'application/json',
    },
});

export default api;