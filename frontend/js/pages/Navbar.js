import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
  <nav>
    <ul>
      <li>
        <Link to="/">Home</Link>
      </li>
      <li>
        <Link to="/restaurants">Restaurants</Link>
      </li>
      {/* Add other links as needed */}
    </ul>
  </nav>
);

export default Navbar;
