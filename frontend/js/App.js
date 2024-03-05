import * as Sentry from "@sentry/react";
import React from "react";
import { Provider } from "react-redux";

//import Home from "./pages/Home";
import configureStore from "./store";
import RestaurantListPage from "./pages/RestaurantListPage";

const store = configureStore({});
const App = () => (
  <Sentry.ErrorBoundary fallback={<p>An error has occurred</p>}>
    <Provider store={store}>
      {/*<Home />*/}
      <RestaurantListPage />
    </Provider>
  </Sentry.ErrorBoundary>
);

export default App;
