import React from "react";
import { Product } from "../products";

interface ProductCardProps {
    product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
    return (
        <div
            style={{
                border: "1px solid #e0e0e0",
                borderRadius: "8px",
                overflow: "hidden",
                boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
                transition: "box-shadow 0.3s",
                width: "300px",
                margin: "10px",
            }}
            onMouseOver={(e) => (e.currentTarget.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.2)")}
            onMouseOut={(e) => (e.currentTarget.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.1)")}
        >
            <div style={{ padding: "15px" }}>
                <h3 style={{ fontSize: "1.5em", fontWeight: "bold", color: "#333", margin: "0 0 10px" }}>
                    {product.name}
                </h3>
                <p style={{ fontSize: "0.9em", color: "#666", margin: "0 0 10px" }}>{product.description}</p>
                <p style={{ fontSize: "1.1em", fontWeight: "bold", color: "#2e7d32", margin: "0 0 10px" }}>
                    ${product.price.toFixed(2)}
                </p>
                <p style={{ fontSize: "0.9em", color: "#757575" }}>
                    <strong>Category:</strong> {product.category} | <strong>Stock:</strong> {product.stock} units
                </p>
            </div>
        </div>
    );
};

export default ProductCard;