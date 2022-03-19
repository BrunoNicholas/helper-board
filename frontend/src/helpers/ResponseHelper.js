/* eslint-disable react-hooks/rules-of-hooks */
import React from "react";
import axios from "axios";

import APIEndpoints from 'helpers/Endpoints';

export default function configureBackend() {
    let users = [];

    // default from example
    let realFetch = window.fetch;
    window.fetch = function (url, opts) {
        const isLoggedIn = opts.headers['Authorization'] === 'Bearer fake-jwt-token';

        return new Promise((resolve, reject) => {
            // authenticate - public
            if (url.endsWith('/login') && opts.method === 'POST') {
                const params = JSON.parse(opts.body);
                const user = users.find(x => x.username === params.username && x.password === params.password);
                if (!user) return error('Username or password is incorrect');
                return ok({
                    id: user.id,
                    username: user.username,
                    firstName: user.firstName,
                    lastName: user.lastName,
                    token: 'fake-jwt-token'
                });
            }

            // get users - secure
            if (url.endsWith('/users') && opts.method === 'GET') {
                if (!isLoggedIn) return unauthorised();
                return ok(users);
            }

            // pass through any requests not handled above
            realFetch(url, opts).then(response => resolve(response));

            // private helper functions

            function ok(body) {
                resolve({ ok: true, text: () => Promise.resolve(JSON.stringify(body)) })
            }

            function unauthorised() {
                resolve({ status: 401, text: () => Promise.resolve(JSON.stringify({ message: 'Unauthorised' })) })
            }

            function error(message) {
                resolve({ status: 400, text: () => Promise.resolve(JSON.stringify({ message })) })
            }
        });
    }
}

// # changes made from tutorial___
// # components/PrivateRoute.jsx -> helpers/CheckAuth.js


// const [post, setPost] = React.useState(null);

//     React.useEffect( () => {
//         axios.get(APIEndpoints.baseURL).then((response) => {
//             setPost(response.data);
//         });
//     }, [] );


// axios.get(URL, { headers: { 'x-access-token': 'TOKEN' } })
// .then(response => {
//     console.log(response.data);
// })
// .catch((error) => {
//     console.log('error ' + error);
// });


