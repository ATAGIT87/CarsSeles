import mysql.connector


def db_connection():
    print("connented/n")
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'test'
    }
    connection = mysql.connector.connect(**config)
    return connection        