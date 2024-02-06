import mysql.connector

# AWS RDS instance details
host = 'hogwarts-hunt-1.cbx57h3ijf7o.eu-north-1.rds.amazonaws.com'
user = 'admin'
password = 'hogwarts'
database = 'heroku_f8e49261e8690a7'
# Establish connection
try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port = "3306"

    )

    if conn.is_connected():
        print('Connected to MySQL database')

        # Fetch all tables
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SHOW TABLES")

        tables = cursor.fetchall()
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table['Tables_in_' + database])
        else:
            print("No tables found in the database")

except Exception as e:
    print(f'Error: {str(e)}')

finally:
    # Close connection when done
    conn.close()
    print('Connection closed')
