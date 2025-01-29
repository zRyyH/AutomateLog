import api from '../axios/axios-instance';
import endpoints from '../endpoint';


// Parar automação
export const fetchStop = async () => {
    try {
        return await api.get(endpoints.STOP);
    } catch (error) {
        throw error;
    }
};


// Iniciar automação
export const fetchStart = async () => {
    try {
        return await api.get(endpoints.START);
    } catch (error) {
        throw error;
    }
};


// Configurar bot de automação
export const fetchSettings = async (payload) => {
    try {
        return await api.post(endpoints.SET, payload);
    } catch (error) {
        throw error;
    }
};