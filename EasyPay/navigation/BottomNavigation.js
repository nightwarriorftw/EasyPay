import React from "react";
import { Ionicons } from "@expo/vector-icons";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import Send from "../screens/Send";
import AtmCard from "../screens/AtmCard";
import Profile from "../screens/Profile";
import Home from "../screens/Home";
const Tab = createBottomTabNavigator();

export default class BottomTabNavigation extends React.Component {
  render() {
    return (
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;
            if (route.name === "Home") {
              iconName = "md-home";
            } else if (route.name === "Send") {
              iconName = "md-navigate";
            } else if (route.name === "Card") {
              iconName = "md-card";
            } else if (route.name === "Profile") {
              iconName = "md-person";
            }
            return <Ionicons name={iconName} size={size} color={color} />;
          }
        })}
        tabBarOptions={{
          activeTintColor: "#9C27B0",
          inactiveTintColor: "black"
        }}
      >
        <Tab.Screen name="Home" component={Home} />
        <Tab.Screen name="Send" component={Send} />
        <Tab.Screen name="Card" component={AtmCard} />
        <Tab.Screen name="Profile" component={Profile} />
      </Tab.Navigator>
    );
  }
}
