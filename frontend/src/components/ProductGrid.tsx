import React, { useState } from "react";
import { dummyProducts, Product } from "../products";
import ProductCard from "./ProductCard";

const ProductGrid: React.FC = () => {
  const [expandedProduct, setExpandedProduct] = useState<string | null>(null);

  const handleToggle = (productId: string) => {
    setExpandedProduct(expandedProduct === productId ? null : productId);
  };

  return (
    <div
      style={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        padding: "20px",
        backgroundColor: "#f5f5f5",
      }}
    >
      {dummyProducts.map((product: Product) => (
        <ProductCard
          key={product.id}
          product={product}
          isExpanded={expandedProduct === product.id}
          onToggle={() => handleToggle(product.id)}
        />
      ))}
    </div>
  );
};

export default ProductGrid;