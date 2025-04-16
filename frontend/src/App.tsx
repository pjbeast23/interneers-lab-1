import React from "react";
import ProductGrid from "./components/ProductGrid";
import "./App.css";

const App: React.FC = () => {
  return (
    <div className="App">
      <h1 style={{ textAlign: "center", color: "#333", padding: "20px" }}>Product Showcase</h1>
      <ProductGrid />
    </div>
  );
};

export default App;