import axios from "axios";
import Endpoints from "helpers/Endpoints";

const API_URL = Endpoints.baseURL + Endpoints.section;

// get all users with token
const getAllNotifications = () => {
    return axios.get(API_URL + Endpoints.routes.notificationsIndex, { headers: Endpoints.authHeader() });
};

// add notification: code coming up
const addNotification = (obj) => {
    if(obj) {

    }
    return 'Error';
}

// get single user profile with token
const getSingleNotification = (id) => {
    return axios.get(API_URL + Endpoints.routes.notificationsIndex + `/${id}`, { headers: Endpoints.authHeader() });
};



// add notification: code coming up
const updateNotification = (obj) => {
    if(obj) {

    }
    return 'Error';
}



// add notification: code coming up
const deleteNotification = (obj) => {
    if(obj) {

    }
    return 'Error';
}

const notificationsService = {
    getAllNotifications,
    getSingleNotification,
    addNotification,
    updateNotification,
    deleteNotification
};

export default notificationsService;