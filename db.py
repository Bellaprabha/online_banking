# c_id=int(input("Enter customer ID:"))
# name=input("Enter customer Name:")
# Account_no=int(input("Enter customer Account_no:"))
# Branch=input("Enter Branch name:")
# IFSC=input("Enter IFSC code:")
# phone=int(input("Enter customer phone number:"))
# address=input("Enter customer Address:")


# import sqlite3 as sql
# con = sql.connect("Customer.db")
# cur = con.cursor()
# #cur.execute("create table c_data(c_id int(8),name str,Account_no int(12),Branch str(50),IFSC varchar(15),phone int(10),Address str(50))")
# cur.execute("insert into c_data values(?,?,?,?,?,?,?)",(c_id,name,Account_no,Branch,IFSC,phone,address))
# con.commit()
# cur.close()
# con.close()