import Index from "pages/index.js";
import Profile from "pages/dashboard/ProfilePage/index.js";
import Message from "pages/dashboard/MessagePage/index.js";
import Notification from "pages/dashboard/NotificationPage/index.js";
import Register from "pages/RegisterPage/index.js";
import Login from "pages/LoginPage/index.js";

var routes = [
  {
    path: "/index",
    name: "Dashboard",
    icon: "ni ni-tv-2 text-primary",
    component: Index,
    layout: "/admin",
  },
  {
    path: "/user-profile",
    name: "User Profile",
    icon: "ni ni-single-02 text-yellow",
    component: Profile,
    layout: "/admin",
  },
  {
    path: "/user-messages",
    name: "Chat Messages",
    icon: "ni ni-single-02 text-yellow",
    component: Message,
    layout: "/admin",
  },
  {
    path: "/user-notifications",
    name: "User Notifications",
    icon: "ni ni-single-02 text-yellow",
    component: Notification,
    layout: "/admin",
  },
  {
    path: "/login",
    name: "Login",
    icon: "ni ni-key-25 text-info",
    component: Login,
    layout: "/auth",
  },
  {
    path: "/register",
    name: "Register",
    icon: "ni ni-circle-08 text-pink",
    component: Register,
    layout: "/auth",
  },
];
export default routes;
