import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book id INTEGER PRIMARY KEY, title text, author text,year integer, isbn integer()")
    conn.commit()
    conn.close()

# ID - THE PRIMARY KEY IS THE AUTO-INCREMENT VALUE SO WE DONT HAVE TO PASS

# the first we need to add the entry function


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


connect()
insert("Moby Dick", "Yang-Lee", 1990, 3625497665)
print(view())
