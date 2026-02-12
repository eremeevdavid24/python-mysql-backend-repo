from db import cursor, connection

def creat_trudent(name):
    query = "INSERT INTO students (name) VALUES (%s)"
    cursor.execute(query, (name,))
    connection.commit()