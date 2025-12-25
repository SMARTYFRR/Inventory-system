# 📦 Inventory Management System  
### Python × MySQL · CLI Based

A clean, beginner-friendly **Inventory Management System** built with **Python** and **MySQL**.  
No GUI. Just basic logic and basic databases.

Runs through the terminal cuz it's CLI based 🥀

---

## ❓ What this does

This project lets you manage inventory records stored in a MySQL database.  
You can add, view, update, delete, and search items, all from a simple CLI menu.

Built to learn:
- Python–MySQL connectivity  
- CRUD operations  
- Modular code structure  
- Real-world database flow  

---

## 🚀 Features

- ➕ Add new inventory items  
- 📋 View all items  
- 🔄 Update item quantity  
- ❌ Delete items  
- 🔍 Search items by name  
- 🗄️ MySQL-backed storage  
- 🧠 Beginner-readable code  

---

## 🗂️ Folder Structure

```bash
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
```

---

## 🛠️ Tech Stack

- Language: Python
- Database: MySQL
- Connector: mysql-connector-python

Install dependencies

```bash
pip install mysql-connector-python
```

---

## 🗄️ Database Setup

Run the SQL file
```bash
database/setup.sql
```
It will:
```
CREATE DATABASE IF NOT EXISTS inventory_db;

USE inventory_db;

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price FLOAT
);
```

---

## 🔧 Configuration

Open ```src/db_connection.py``` 
and update your MySQL password:
````password = "your_password_here````
Make sure MySQL server is running.

---

## ▶️ Run the Project

From the project root:

```python main.py```

You'll get a CLI menu.

Pick options by typing numbers.

Simple as that.

--- 

## 🤝 Contributions 

This is an **eductaional project**.

Fork it. 

IMprove it.

Add feature.

Break it.

Fix it.

depends on you.

---

## 📜 License

Open-source.

Free to use.

Learn, build, and don't gatekeep knowledge.

---

## ⭐ Final Note 

Thank you for visiting my project!

if this repo helped you even a little or you liked it

Drop a ⭐ and keep shipping.

~**Anshu** 
