import pyodbc

server = 'cstnt.tstc.edu'
database = 'itse2359sp21'
username = 'acortezsp212359'
password = '1628893'

con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = con.cursor()
#selectQuery = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE 'm%'")
#selectHardwareQuery = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term = 'hardware'")
#selectSInTerm = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE '%s%'")
#selectContainsWare = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE '%ware%'")
selectTermEndT = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term LIKE '%t'")

results = cursor.fetchall()

for result in results:
        print(result)
