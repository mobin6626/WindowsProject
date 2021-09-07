import sqlite3


def connect():
    conn = sqlite3.connect("../:memory:")
    cur = conn.cursor()
    cur.execute(
       "CREATE TABLE IF NOT EXISTS list (id INTEGER PRIMARY KEY , name text , number INTEGER ,"
       " price INTEGER, tip INTEGER , waiter text)"
    )
    conn.commit()
    conn.close()

def insert(name, number, price, tip, waiter):
    conn = sqlite3.connect("../:memory:")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO list VALUES (NULL ,?,?,?,?,?)", (name, number, price, tip, waiter)
    )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("../:memory:")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM list"
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("../:memory:")
    cur = conn.cursor()
    cur.execute("DELETE FROM list WHERE id=?", (id,))
    conn.commit()
    conn.close()


connect()
