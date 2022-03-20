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
        if(response.data.errors) {
            let errMsg = ``;
            response.data.errors.forEach(function(err){
                if (err.name) {
                    errMsg = errMsg + `Name\n`;
                    for (let i = 0; i < err.name.length; i++) {
                        errMsg = errMsg + `- ${err.name[i]}\n`;
                    }
                    console.log('ITEMS: ', errMsg);
                }
        
                if (err.email) {
                    errMsg = errMsg + `Email\n`;
                    for (let i = 0; i < err.email.length; i++) {
                        errMsg = errMsg + `- ${err.email[i]}\n`;                  
                    }
                    console.log('ITEMS: ', errMsg);
                }

                if (err.password) {
                    errMsg = errMsg + `Password\n`;
                    for (let i = 0; i < err.password.length; i++) {
                        errMsg = errMsg + `- ${err.password[i]}\n`;
                    }
                    console.log('ITEMS: ', errMsg);
                }
            });
            swal("Validation errors", errMsg, "error");
        }
        else if (response.data.message) {
            swal("Success", response.data.message, "success");
        }
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

const checkIsUserValid = () => {
    axios.get(API_URL + Endpoints.routes.user, { headers: Endpoints.headers })
    .then((res) => {
        if (res.data.email === getCurrentUser().user.email) {                
            let gotUser = getCurrentUser();
            gotUser.user = res.data;
            localStorage.setItem("user", JSON.stringify(gotUser));

            swal(`Hello ${gotUser.user.name}`, "Welcome back!", "success");
            
            localStorage.setItem("userAuthVal", 'true');
        }
        else {
            swal(`Hey ${getCurrentUser().user.name}, your previous section expired.\nPlease login again!`)
            .then(() => {
                logout();
                // code to redirect to login
            });
            localStorage.setItem("userAuthVal", 'false');
        }
    })
    .catch((err) => {
        swal("Unauthenticated", "Hello, please login to view your dashboard", "info");
        localStorage.setItem("userAuthVal", 'false');
        logout();
    });
}

const authService = {
    signup,
    login,
    logout,
    getCurrentUser,
    checkIsUserValid
};

export default authService;