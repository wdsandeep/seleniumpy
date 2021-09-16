import mysql.connector

mydb = mysql.connector.connect( host = "localhost", user="root", passwd="sandeep", database="NewTestDB"  )

mycursor =  mydb.cursor() 

#mycursor.execute("SELECT id FROM jos_downloads_containers");
#result = mycursor.fetchall()
#
#for i in mycursor:
#    print(i)
#
#print("Hello")


