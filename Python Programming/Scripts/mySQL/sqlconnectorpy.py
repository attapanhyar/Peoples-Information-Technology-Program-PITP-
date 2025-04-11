# pip install mysql.connector
import mysql.connector
conn = None
try:
     conn = mysql.connector.connect(host='localhost', 
                                   port=3306,
                                   database='northwind',
                                   user='root',
                                   password='Gh0tki786@@')
     if conn.is_connected():
        print('Connected to MySQL database')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers where city = \'London\'")
        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
except mysql.connector.Error as e:
    # Print an error message if a connection error occurs
    print(e)
finally:
    # Close the database connection in the 'finally' block to ensure it happens
    if conn is not None and conn.is_connected():
        conn.close()
