import React from "react";
import { dummyProducts, Product } from "../products";
import ProductCard from "./ProductCard";

const ProductGrid: React.FC = () => {
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
                <ProductCard key={product.id} product={product} />
            ))}
        </div>
    );
};

export default ProductGrid;