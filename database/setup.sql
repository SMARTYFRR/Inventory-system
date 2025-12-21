CREATE DATABASE IF NOT EXISTS inventory_db;

USE inventory_db;

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price FLOAT
);
