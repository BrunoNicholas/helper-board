import axios from "axios";
import Endpoints from "helpers/Endpoints";

const API_URL = Endpoints.baseURL + Endpoints.section;

// get all users with token
const getAllMessages = () => {
    return axios.get(API_URL + Endpoints.routes.messagesIndex, { headers: Endpoints.authHeader() });
};

// add notification: code coming up
const addMessage = (obj) => {
    if(obj) {

    }
    return 'Error';
}

// get single user profile with token
const getSingleMessage = (id) => {
    return axios.get(API_URL + Endpoints.routes.messagesIndex + `/${id}`, { headers: Endpoints.authHeader() });
};



// add notification: code coming up
const updateMessage = (obj) => {
    if(obj) {

    }
    return 'Error';
}



// add notification: code coming up
const deleteMessage = (obj) => {
    if(obj) {

    }
    return 'Error';
}

const messagesService = {
    getAllMessages,
    getSingleMessage,
    addMessage,
    updateMessage,
    deleteMessage
};

export default messagesService;