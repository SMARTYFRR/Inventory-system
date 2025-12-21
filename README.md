📦 Inventory Management System (Python + MySQL)

A simple and beginner-friendly Inventory Management System built using Python and MySQL.
This project lets users manage items by adding, viewing, updating, deleting, and searching records stored inside a MySQL database.

🚀 Features

Add new items to inventory

View all items

Update item quantity

Delete items

Search items by name

Uses MySQL database for storing data

Clean modular code (easy to understand)


inventory_system/
│
├── main.py
│
├── src/
│   ├── db_connection.py
│   └── inventory_functions.py
│
└── database/
    └── setup.sql


🛠️ Requirements

Python 3.x

MySQL Server & MySQL Workbench

MySQL Connector for Python

Install MySQL connector using: pip install mysql-connector-python

🗄️ Database Setup

Run the SQL script inside database/setup.sql.

It will automatically:

Create the database inventory_db

Create the table items


SQL structure:
CREATE DATABASE IF NOT EXISTS inventory_db;

USE inventory_db;

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price FLOAT
);

🔧 Configure Database Connection

Inside src/db_connection.py, update your MySQL password: password="your_password_here"


Running the Program

Open terminal inside the project folder and run: python main.py
This will open the CLI menu
Choose any option by typing its number.

🤝 Contribution

This is a simple educational project.
Feel free to fork and add new features.

📜 License

This project is open-source and free to use.
