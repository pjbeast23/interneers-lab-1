import React from "react";
import Header from "./components/Header";
import ProductList from "./components/ProductList";
import "./App.css";

const App: React.FC = () => {
  return (
    <div className="App">
      <Header />
      <main>
        <h1 style={{ textAlign: "center", color: "#333", padding: "20px" }}>Product Showcase</h1>
        <ProductList />
      </main>
    </div>
  );
};

export default App;