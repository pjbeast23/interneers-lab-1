import React, { useState } from "react";
// Use type-only import for the Product interface
import type { Product } from "../products";
import ProductItem from "./ProductItem";
import { dummyProducts } from "../products";

const ProductList: React.FC = () => {
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
        <ProductItem
          key={product.id}
          product={product}
          isExpanded={expandedProduct === product.id}
          onToggle={() => handleToggle(product.id)}
        />
      ))}
    </div>
  );
};

export default ProductList;