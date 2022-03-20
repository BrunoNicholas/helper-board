const storedStr = localStorage.getItem("user");
const user = JSON.parse(storedStr);
let authHeader = {}

if (storedStr && user && user.token) {
    authHeader = {
        'x-access-token': user.token,
        'Content-Type': 'application/json'
    };
} else {
    authHeader = {
        'Content-Type': 'application/json'
    };
}

const APIEndpoints = {
    baseURL: 'http://localhost:5050',
    section: '/api/v1',
    headers: authHeader,
    routes: {
        login: '/login',
        register: '/signup',
        user: '/user',
        usersIndex: '/users',
        messagesIndex: '/messages',
        locationsIndex: '/locations',
        notificationsIndex: '/notifications'
    }
}

export default APIEndpoints;