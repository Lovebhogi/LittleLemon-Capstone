import mysql.connector
from mysql.connector import Error

def manage_booking_via_python(cursor, connection, b_id, c_id, b_date, t_no):
    try:
        cursor.execute(f"INSERT IGNORE INTO customer (customer_id, full_name, contact_number) VALUES ({c_id}, 'Test Customer', '555-0199')")
        
        cursor.callproc('AddBooking', (b_id, c_id, b_date, t_no))
       
        connection.commit()
        print(f"Procedure executed: Booking {b_id} successfully added for table {t_no}.")
        
    except Error as e:
        print(f"Failed to execute procedure: {e}")

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='littlelemondb',
        user='root',
        password='root' 
    )

    if connection.is_connected():
        print("Successfully connected to the Little Lemon database.")
        cursor = connection.cursor()
        
        manage_booking_via_python(cursor, connection, 1, 1, '2026-10-20 19:00:00', 5)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")