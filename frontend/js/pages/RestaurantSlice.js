import { createSlice } from "@reduxjs/toolkit";

const restaurantsSlice = createSlice({
  name: "restaurants",
  initialState: {
    list: [],
  },
  reducers: {
    setRestaurants: (state, action) => {
      state.list = action.payload;
    },
  },
});

export const { setRestaurants } = restaurantsSlice.actions;
export const selectRestaurants = (state) => state.restaurants.list;
export default restaurantsSlice.reducer;
