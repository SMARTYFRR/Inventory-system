import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cr7isdagoat",   #put yo my SQL pass here ngga
        database="inventory_db"
    )
