import sqlite3

# now its all organises to this one true indent. 
class Database:

    def __init__(self, db):
        # __init__  func is to initialise the object
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text,year integer, isbn integer)")
        conn.commit()
        conn.close()

    # ID - THE PRIMARY KEY IS THE AUTO-INCREMENT VALUE SO WE DONT HAVE TO PASS

    # the first we need to add the entry function

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)",
                    (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM  book WHERE title=? OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE  id=?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE  id=?",
                    (title, author, year, isbn, id))
        conn.commit()
        conn.close()


# connect()
# insert("Moby Dick", "Yang-Lee", 1990, 3625497665)
# insert("The Martian", "something something", 2015, 5698521475)
# delete(2)

# update(6, "All the bright places",
#        "someone's writing style i like the most", 2020, 9101821000)
# print(view())
# print(search(author="Yang-Lee"))
