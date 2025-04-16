export interface Product {
  id: string;
  name: string;
  price: number;
  description: string;
  stock: number;
  category: string;
}

export const dummyProducts: Product[] = [
  {
    id: "1",
    name: "Laptop Pro",
    price: 1299.99,
    description: "High-performance laptop with 16GB RAM",
    stock: 45,
    category: "Electronics",
  },
  {
    id: "2",
    name: "Smartphone X",
    price: 799.99,
    description: "Latest model with 5G support",
    stock: 120,
    category: "Electronics",
  },
  {
    id: "3",
    name: "Cotton Jacket",
    price: 49.99,
    description: "Stylish and warm cotton jacket",
    stock: 150,
    category: "Clothing",
  },
];