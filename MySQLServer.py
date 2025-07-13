import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (change user and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234567890'  # ← Replace this with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as err:
        print(f"Error: {err}")

    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
