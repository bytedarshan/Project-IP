import mysql.connector
import importlib
print("                      |----------------------------------------------------------------------|")
print("                      |                              DATA ENTRY                              |")
print("                      |----------------------------------------------------------------------|")
print("                      |                                                                      |")

# Establish database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="useradmin@100",
    database="IPPROJECT"
)

cursor = db.cursor()

# Execute SELECT query to get the existing barcode numbers
cursor.execute("SELECT BARCODE_NUMBER FROM STOCK")

# Fetch all rows
results = cursor.fetchall()

# Create a list of barcode numbers
column_values = [row[0] for row in results]


# Taking input from the user
try:
    barcode_number = int(input("                      |            Enter the BARCODE NUMBER: "))
    name_item = input("                      |            Enter the NAME OF ITEM: ")
    qty = int(input("                      |            Enter the QUANTITY: "))
    mrp = int(input("                      |            Enter the MRP: "))
    srp = int(input("                      |            Enter the SRP: "))
    
    # Check if barcode_number is in the existing stock
    if barcode_number in column_values:  # Specific check for a barcode
        query="SELECT BARCODE_NUMBER, NAME_OF_ITEM, QUANTITY, MRP, SRP FROM STOCK WHERE BARCODE_NUMBER=%s"
        cursor.execute(query, (barcode_number,))
        #Fetch the first row (if it exists)
        row = cursor.fetchone()
        barcode_number, name_of_item, quantity, mrp, srp = row
        update_query = ("UPDATE STOCK SET QUANTITY = %s "
                        "WHERE BARCODE_NUMBER = %s")
        new_value = quantity + qty  # Adjust this logic if needed
        condition_value = barcode_number
        cursor.execute(update_query, (new_value, condition_value))
        db.commit()  # Commit the update
        print("                      |----------------------------------------------------------------------|")
        print('                      |                              Item Updated                            |')
        
    else:
        query = "INSERT INTO STOCK (BARCODE_NUMBER, NAME_OF_ITEM, QUANTITY, MRP, SRP) VALUES (%s, %s, %s, %s, %s);"
        values = (barcode_number, name_item, qty, mrp, srp)
        cursor.execute(query, values)
        db.commit()  # Commit the insert
        print("                      |----------------------------------------------------------------------|")
        print("                      |                          Item added to stock                         |")

except mysql.connector.Error as err:
    print(f"                       Database error: {err}")
except ValueError:
    print("                      |Please enter valid numeric values for barcode, quantity, MRP, and SRP.|")
finally:
    cursor.close()
    db.close()
print("                      |----------------------------------------------------------------------|")
print("")
print("")
print("")
print("                      |----------------------------------------------------------------------|")
print("                      |                  TO ADD OR UPDATE ANOTHER ENTRY PRESS 1              |")
print("                      |                  PRESS ANY OTHER KEY TO EXIT                         |")
print("                      |----------------------------------------------------------------------|")
a=input("                                         Enter here :")
print("                      |----------------------------------------------------------------------|")
if a=='1':
    import entry
    importlib.reload(entry)
else:
    print("                      |                              THANK YOU                               |")
    print("                      |----------------------------------------------------------------------|")
