import React, { useState, useEffect } from "react";
import axios from "axios";

const RestaurantsPage = () => {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Fetch restaurants data from your API
    axios
      .get("/api/restaurant")
      .then((response) => {
        setRestaurants(response.data);
      })
      .catch((error) => {
        console.error("Error fetching restaurants:", error);
      });
  }, []);

  return (
    <div>
      <h1>Restaurants</h1>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <strong>{restaurant.name}</strong>
            <ul>
              {restaurant.recipes.map((recipe) => (
                <li key={recipe.id}>{recipe.name}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RestaurantsPage;
