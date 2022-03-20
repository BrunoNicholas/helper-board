import axios from "axios";
import Endpoints from 'helpers/Endpoints';

const API_URL = Endpoints.baseURL + Endpoints.section;

const signup = (email, password) => {
    return axios.post(API_URL + Endpoints.routes.register, {
        email,
        password,
    }, { headers: Endpoints.authHeader })
    .then((response) => {
        if (response.data.accessToken) {
            localStorage.setItem("user", JSON.stringify(response.data));
        }
        return response.data;
    })
    .catch(() => {
        alert('signup failed');
    });
};

const login = (email, password) => {
    console.log("Endpoint");
    console.log(API_URL + Endpoints.routes.login);
    console.log("Data");
    console.log(`EMAIL: ${email}, PASSWORD: ${password}`);
    console.log("Headers");
    console.log(Endpoints.authHeader);
    return axios.post(API_URL + Endpoints.routes.login, {
        email,
        password,
    }, { headers: Endpoints.authHeader })
    .then((response) => {
        console.log(response);
        if (response.data.accessToken) {
            localStorage.setItem("user", JSON.stringify(response.data));
        }
        return response.data;
    })
    .catch((ee) => {
        console.log(ee)
        alert('authentication failed');
    });
};

const logout = () => {
    localStorage.removeItem("user");
};

const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem("user"));
};

const authService = {
    signup,
    login,
    logout,
    getCurrentUser,
};

export default authService;