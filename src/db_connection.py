import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_real_password",   #put yo my SQL pass here ngga
        database="inventory_db"
    )
