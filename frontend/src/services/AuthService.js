import axios from "axios";
import Endpoints from 'helpers/Endpoints';
import swal from 'sweetalert';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const createNotification = (type, msg='', posn='top-left', tym=3000) => {
    return () => {
        switch (type) {
            case 'info':
                toast.info(msg, {
                    position: "top-left",
                    autoClose: tym,
                    hideProgressBar: false,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                });
                break;
            case 'success':
                toast.success(msg, {
                    position: "top-left",
                    autoClose: tym,
                    hideProgressBar: false,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                });
                break;
            case 'warning':
                toast.warn(msg, {
                    position: "top-left",
                    autoClose: tym,
                    hideProgressBar: false,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                });
                break;
            case 'error':
                toast.error(msg, {
                    position: "top-left",
                    autoClose: tym,
                    hideProgressBar: false,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                });
                break;
            default:
                toast(msg, {
                    position: "top-left",
                    autoClose: tym,
                    hideProgressBar: false,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                });
                break;
        }
    };
};

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
            setTimeout(function(){
                window.location.reload();
            },3000);
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

            // swal(`Hello ${gotUser.user.name}`, "Welcome back!", "success");
            createNotification('success',`Hello ${gotUser.user.name}, Welcome back! success`);
            
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
    checkIsUserValid,
    createNotification
};

export default authService;