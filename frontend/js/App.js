import * as Sentry from "@sentry/react";
import React from "react";
import { Provider } from "react-redux";

import Home from "./pages/Home";
import configureStore from "./store";
import RecipeView from './pages/RecipeView';
import RecipeListView from './pages/RecipeListView';
import RecipeEntry from './pages/RecipeEntry';
import ScrapeRecipePage from './pages/ScrapeRecipePage';
import RestaurantsPage from "./pages/RestaurantsPage";

const store = configureStore({});
const App = () => (
  <Sentry.ErrorBoundary fallback={<p>An error has occurred</p>}>
    <Provider store={store}>
      {/*<Home />*/}
      <RestaurantsPage />
      <RecipeView />
      <RecipeEntry />
      <RecipeListView />
      <ScrapeRecipePage />
    </Provider>
  </Sentry.ErrorBoundary>
);

export default App;
