import { combineReducers } from "@reduxjs/toolkit";

import { restCheckReducer as restCheck } from "./rest_check";
import restaurantsReducer from "../pages/RestaurantSlice";  // Import the restaurantsReducer


export const rootReducer = combineReducers({
  restaurants: restaurantsReducer,
  restCheck,
});
