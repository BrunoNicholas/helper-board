function authHeader() {
    const user = JSON.parse(localStorage.getItem("user"));
  
    if (user && user.token) {
        return {
            'x-access-token': user.token,
            'Content-Type': 'application-json'
        };
    } else {
        return {
            'Content-Type': 'application-json'
        };
    }
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