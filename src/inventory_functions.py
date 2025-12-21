from src.db_connection import get_connection


def add_item(name, qty, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO items (name, quantity, price) VALUES (%s, %s, %s)",
        (name, qty, price)
    )
    conn.commit()
    conn.close()

def view_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_item(item_id, qty):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET quantity = %s WHERE id = %s",
        (qty, item_id)
    )
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM items WHERE id = %s", 
        (item_id,)
    )
    conn.commit()
    conn.close()

def search_item(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM items WHERE name LIKE %s",
        (f"%{name}%",)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
