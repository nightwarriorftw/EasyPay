import { createStackNavigator } from "react-navigation-stack";
import Welcome from "../screens/Welcome.js";
import Register from "../screens/authentication/Register.js";
import BvnScreen from "../screens/authentication/BvnScreen";
import ConfirmUpload from "../screens/ConfirmUpload";
import UploadScreen from "../screens/authentication/UploadScreen";
import Login from "../screens/authentication/Login.js";
import ForgotPassword from "../screens/authentication/ForgotPassword.js";
const AuthNavigation = createStackNavigator(
  {
    Welcome: Welcome,
    Login: Login,
    Register: Register,
    Confirm: ConfirmUpload,
    UploadScreen: UploadScreen,
    Bvn: BvnScreen,
    ForgotPassword: ForgotPassword
  },
  {
    headerMode: "none"
  }
);

export default AuthNavigation;
