import  mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "rot",
    password = "root",
    database = "backend_database"
)

cursor = connection.cursor()