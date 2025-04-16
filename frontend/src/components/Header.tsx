import React from "react";
import "./Header.css";

const Header: React.FC = () => {
  return (
    <header>
      <div className="header-container">
        <h1 className="logo">My Store</h1>
        <nav>
          <ul className="nav-list">
            <li><a href="/" className="nav-link">Home</a></li>
            <li><a href="/products" className="nav-link">Products</a></li>
            <li><a href="/about" className="nav-link">About</a></li>
          </ul>
          <button className="hamburger">☰</button>
        </nav>
      </div>
    </header>
  );
};

export default Header;