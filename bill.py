import mysql.connector
import csv

# Establish database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="useradmin@100",
    database="IPPROJECT"
)

cursor = db.cursor()

name=input("Enter the Name of Customer :")
number=input("Enter the Mobile Number :")

# Example SELECT query to fetch a row from the "users" table
barcode_number=int(input("Enter the barcode number :"))
query="SELECT BARCODE_NUMBER, NAME_OF_ITEM, QUANTITY, MRP, SRP FROM STOCK WHERE BARCODE_NUMBER=%s"
cursor.execute(query, (barcode_number,))
# Fetch the first row (if it exists)
row = cursor.fetchone()

# Check if the row is not None (empty result set)
if row:
    # Extract values from the row and assign them to different variables
    barcode_number, name_of_item, quantity, mrp, srp = row

    # Now you can use the variables `user_id`, `username`, `email`, and `age`
    print(f"BARCODE NUMBER: {barcode_number}")
    print(f"NAME OF ITEM: {name_of_item}")
    print(f"QUANTITY: {quantity}")
    print(f"MRP: {mrp}")
    print(f"SRP: {srp}")
else:
    print("Item Not Found")

qty=int(input("Enter the quantity required :"))
print("------------------Bill------------------")
print("Buyer's Name -",name)
print("Contact Number -",number)
print("----------------------------------------")
print("----------------------------------------")
print("Name of item -",name_of_item)
print("Quantity -",qty)
print("Price -",srp,'/-')
tax=srp*0.18
print("Tax -",tax,'/-')
total=(srp+tax)*qty
print("Total -",total,'/-')
print("----------------------------------------")
update_query = ("UPDATE STOCK SET QUANTITY = %s "
                "WHERE BARCODE_NUMBER = %s")
new_value = quantity - qty  # Adjust this logic if needed
condition_value = barcode_number
cursor.execute(update_query, (new_value, condition_value))
db.commit()  # Commit the update






# Open a file in write mode
with open('output.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write header (optional)
    writer.writerow(["Name", "Mobile Number", "Item", "Quantity", "Price", "Tax", "Total"])
    
    # Write data rows
    writer.writerow([name,number,name_of_item,qty,srp,tax,total])

print("Data exported to CSV file successfully.")
