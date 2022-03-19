import axios from "axios";
import Endpoints from "helpers/Endpoints";

const API_URL = Endpoints.baseURL + Endpoints.section;

// get all users with token
const getAllUsers = () => {
    return axios.get(API_URL + Endpoints.routes.usersIndex, { headers: Endpoints.authHeader() });
};

// get single user profile with token
const getSingleUser = (id) => {
    return axios.get(API_URL + Endpoints.routes.usersIndex + `/${id}`, { headers: Endpoints.authHeader() });
};

const userService = {
  getAllUsers,
  getSingleUser
};

export default userService;