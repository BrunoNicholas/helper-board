import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";

import "assets/plugins/nucleo/css/nucleo.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "assets/scss/argon-dashboard-react.scss";
import 'react-notifications/lib/notifications.css';
import 'react-toastify/dist/ReactToastify.css';

import AdminLayout from "layouts/Admin.js";
import AuthLayout from "layouts/Auth.js";
import authService from 'services/AuthService';

function routerCheck() {
  authService.checkIsUserValid();
  if (localStorage.getItem("userAuthVal") === 'true') {
    return <Redirect from="/" to="/admin/index" />;
  }
  return <Redirect from="/" to="/auth/login" />;
}

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/admin" render={(props) => <AdminLayout {...props} />} />
      <Route path="/auth" render={(props) => <AuthLayout {...props} />} />
      { routerCheck() }
    </Switch>
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
