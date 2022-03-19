import axios from "axios";
import Endpoints from "helpers/Endpoints";

const API_URL = Endpoints.baseURL + Endpoints.section;

// get all users with token
const getAllNotifications = () => {
    return axios.get(API_URL + Endpoints.routes.locationsIndex, { headers: Endpoints.authHeader() });
};

// add notification: code coming up

// get single user profile with token
const getSingleNotification = (id) => {
    return axios.get(API_URL + Endpoints.routes.locationsIndex + `/${id}`, { headers: Endpoints.authHeader() });
};

const locationsService = {
  getAllNotifications,
  getSingleNotification
};

export default locationsService;