import axios from "axios";
import Endpoints from "helpers/Endpoints";

const API_URL = Endpoints.baseURL + Endpoints.section;

// get all users with token
const getAllLocations = () => {
    return axios.get(API_URL + Endpoints.routes.locationsIndex, { headers: Endpoints.authHeader() });
};

// add notification: code coming up
const addLocation = (obj) => {
    if(obj) {

    }
    return 'Error';
}

// get single user profile with token
const getSingleLocation = (id) => {
    return axios.get(API_URL + Endpoints.routes.locationsIndex + `/${id}`, { headers: Endpoints.authHeader() });
};



// add notification: code coming up
const updateLocation = (obj) => {
    if(obj) {

    }
    return 'Error';
}



// add notification: code coming up
const deleteLocation = (obj) => {
    if(obj) {

    }
    return 'Error';
}

const locationsService = {
    getAllLocations,
    getSingleLocation,
    addLocation,
    updateLocation,
    deleteLocation
};

export default locationsService;