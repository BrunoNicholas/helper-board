import axios from "axios";
import Endpoints from 'helpers/Endpoints';
import swal from 'sweetalert';

const API_URL = Endpoints.baseURL + Endpoints.section;

const signup = (email, password) => {
    return axios.post(API_URL + Endpoints.routes.register, 
        {email, password},
        { headers: Endpoints.headers }
    )
    .then((response) => {
        console.log(response);
        if (response.data.token) {
            localStorage.setItem("user", JSON.stringify(response.data));
        }
        return response.data;
    })
    .catch((ee) => {
        // console.log(ee);
        alert('signup failed');
    });
};

const login = (email, password) => {
    return axios.post(API_URL + Endpoints.routes.login,
        { 'email': email, 'password': password },
        { headers: Endpoints.headers }
    )
    .then((response) => {
        console.log(response);
        if (response.data.token) {
            localStorage.setItem("user", JSON.stringify(response.data));
        }
        if (response.data.message) {
            swal("Success", response.data.message, "success");
        }
        // if(response.data.errors) {
        //     let errMsg = '';
        //     // response.data.errors.forEach(function(item){
        //     //     errMsg = errMsg + `- ${item}\n`;
        //     // });
        //     swal("Validation errors", errMsg, "error");
        // }
        return response.data;
    })
    .catch(() => {
        swal("Connection Error", "There is an error with the connection, Please contact the administrator to fix it", "error");
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