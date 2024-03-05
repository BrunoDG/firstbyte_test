// frontend/src/pages/RestaurantListPage.js
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { setRestaurants, selectRestaurants } from "../pages/RestaurantSlice";

const RestaurantListPage = () => {
  const dispatch = useDispatch();
  const restaurants = useSelector(selectRestaurants);

  useEffect(() => {
    // Fetch the list of restaurants and dispatch the action to store the data in Redux
    axios
      .get("/api/restaurants") // Adjust the API endpoint
      .then((response) => {
        dispatch(setRestaurants(response.data));
      })
      .catch((error) => {
        console.error("Error fetching restaurants:", error);
      });
  }, [dispatch]);

  return (
    <div>
      <h1>Restaurant List</h1>
      {restaurants.map((restaurant) => (
        <div key={restaurant.id}>
          <h2>{restaurant.name}</h2>
          <ul>
            {restaurant.recipes.map((recipe) => (
              <li key={recipe.id}>{recipe.name}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default RestaurantListPage;
