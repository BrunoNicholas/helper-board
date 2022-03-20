import React from 'react';
import { Route, Redirect } from 'react-router-dom';

import { authenticationService } from 'services/AuthService';

export const PrivateRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={props => {
        const currentUser = authenticationService.currentUserValue;
        if (currentUser) {
            // logged in so redirect to dashbosrd page with the return url
            return <Redirect to={{
                pathname: '/admin/index',
                state: { from: props.location }
            }} />
        }

        // not authorised so return component
        return <Component {...props} />
    }} />
)