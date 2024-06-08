import mysql.connector 
 
# connecting to the database 
dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "root",
                     passwd = "",
                     database = "mydatabase" )  
 
# preparing a cursor object 
cursorObject = dataBase.cursor() 
 
# creating table  
studentRecord = """CREATE TABLE EMPLOYEE ( 
                   USERNAME  VARCHAR(20) NOT NULL, 
                   PASSWORD  VARCHAR(20) NOT NULL
                   )"""
 
# table created
cursorObject.execute(studentRecord)  
 
# disconnecting from server
dataBase.close()