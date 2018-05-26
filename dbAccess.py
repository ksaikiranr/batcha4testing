import sqlite3

UsersDB = "UsersDB"
usersTable = "users"
ItemsDB = "ItemsDB"

#adminsTable = "adminsTable"
#salaryTable = "salaryTable"
#propertyTable = "propertyTable"
#bankTable = "bankTable"
#vehicleTable = "vehicleTable"

adminsTable = "taxDeptDB"
salaryTable = "taxDeptDB"
propertyTable = "taxDeptDB"
bankTable = "taxDeptDB"
vehicleTable = "taxDeptDB"
managersTable = "taxDeptDB"
administratorTable  = "taxDeptDB"
feedbacksTable = "taxDeptDB"



####               Managers   Table     #############
def createFeedbacksTable():
	conn = sqlite3.connect(feedbacksTable + ".sqlite")
	curs = conn.cursor()
	id = "feedback"
	curs.execute("create table if not exists " + id + "(id INTEGER PRIMARY KEY AUTOINCREMENT, emailid TEXT, name TEXT, subject TEXT, message TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addFeedback(emailid,name,subject,message,dateTime):
	conn = sqlite3.connect(feedbacksTable + ".sqlite")
	curs = conn.cursor()
	id = "feedback"
	curs.execute("insert into "+ id +" values(?,?,?,?,?,?)",(None,emailid, name, subject,message,dateTime))
	conn.commit()
	curs.close()
	conn.close()

def getFeedbacks():
	conn = sqlite3.connect(feedbacksTable + ".sqlite")
	curs = conn.cursor()
	id = "feedback"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows



####               Administrator   Table     #############
def createAdminstTable():
	conn = sqlite3.connect(administratorTable + ".sqlite")
	curs = conn.cursor()
	id = "adminst"
	curs.execute("create table if not exists " + id + "(id INTEGER PRIMARY KEY AUTOINCREMENT, emailid TEXT, name TEXT, password TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addAdminst(emailid,adminName,password):
	conn = sqlite3.connect(administratorTable + ".sqlite")
	curs = conn.cursor()
	id = "adminst"
	print("#################################")
	print(emailid,adminName,password)
	curs.execute("insert into "+ id +" values(?,?,?,?)",(None,emailid, adminName, password))
	conn.commit()
	curs.close()
	conn.close()

def getAdminst():
	conn = sqlite3.connect(administratorTable + ".sqlite")
	curs = conn.cursor()
	id = "adminst"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows




####               Managers   Table     #############
def createManagersTable():
	conn = sqlite3.connect(managersTable + ".sqlite")
	curs = conn.cursor()
	id = "manager"
	curs.execute("create table if not exists " + id + "(id INTEGER PRIMARY KEY AUTOINCREMENT, emailid TEXT, name TEXT, password TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addManager(emailid,adminName,password):
	conn = sqlite3.connect(managersTable + ".sqlite")
	curs = conn.cursor()
	id = "manager"
	print("#################################")
	print(emailid,adminName,password)
	curs.execute("insert into "+ id +" values(?,?,?,?)",(None,emailid, adminName, password))
	conn.commit()
	curs.close()
	conn.close()

def getManagers():
	conn = sqlite3.connect(managersTable + ".sqlite")
	curs = conn.cursor()
	id = "manager"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows


####               ADMINS   Table     #############
def createAdminsTable():
	conn = sqlite3.connect(adminsTable + ".sqlite")
	curs = conn.cursor()
	id = "admins"
	curs.execute("create table if not exists " + id + "(id INTEGER PRIMARY KEY AUTOINCREMENT, emailid TEXT, name TEXT, password TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addAdmin(emailid,adminName,password):
	conn = sqlite3.connect(adminsTable + ".sqlite")
	curs = conn.cursor()
	id = "admins"
	print("#################################")
	print(emailid,adminName,password)
	curs.execute("insert into "+ id +" values(?,?,?,?)",(None,emailid, adminName, password))
	conn.commit()
	curs.close()
	conn.close()

def getAdmins():
	conn = sqlite3.connect(adminsTable + ".sqlite")
	curs = conn.cursor()
	id = "admins"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows

####            Salary Table	  ####
def createSalaryTable():
	conn = sqlite3.connect(salaryTable + ".sqlite")
	curs = conn.cursor()
	id = "salary"
	curs.execute("create table if not exists " + id + "(aadhar TEXT PRIMARY KEY, name TEXT,salary TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addPersonSalary(aadhar,name,salary):
	conn = sqlite3.connect(salaryTable + ".sqlite")
	curs = conn.cursor()
	id = "salary"
	curs.execute("insert into "+ id +" values(?,?,?)",(aadhar,name,salary))
	conn.commit()
	curs.close()
	conn.close()


def updatePersonSalary(id,name,salary):
	conn = sqlite3.connect(salaryTable + ".sqlite")
	curs = conn.cursor()
	id = "salary"
	curs.execute("update " + id + " set name = ?, salary = ? where aadhar = '"+id+"'",(name,salary))
	conn.commit()
	curs.close()
	conn.close()

def deletePerson(aadharId):
	conn = sqlite3.connect(salaryTable + ".sqlite")
	curs = conn.cursor()
	id = "salary"
	curs.execute("delete from " + id + " where aadhar = '"+aadharId+"'")
	conn.commit()
	curs.close()
	conn.close()

def getSalaryTable():
	conn = sqlite3.connect(salaryTable + ".sqlite")
	curs = conn.cursor()
	id = "salary"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows


def getIds():
	conn = sqlite3.connect(salaryTable + ".sqlite")
	curs = conn.cursor()
	id = "salary"
	curs.execute("select aadhar, name from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows


####            Property Table	  ####
def createPropertyTable():
	conn = sqlite3.connect(propertyTable + ".sqlite")
	curs = conn.cursor()
	id = "property"
	curs.execute("create table if not exists " + id + "(aadhar TEXT PRIMARY KEY, owner TEXT, propertyName Text, estimateVal TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addProperty(aadhar,owner,propertyNam, estVal):
	conn = sqlite3.connect(propertyTable + ".sqlite")
	curs = conn.cursor()
	id = "property"
	curs.execute("insert into "+ id +" values(?,?,?,?)",(aadhar,owner,propertyNam,estVal))
	conn.commit()
	curs.close()
	conn.close()

def updateProperty(aadhar,owner,propertyNam, estVal):
	conn = sqlite3.connect(propertyTable + ".sqlite")
	curs = conn.cursor()
	id = "property"
	curs.execute("update " + id + " set owner = ?, propertyName = ?, estimateValue = ? where aadhar = '"+aadhar+"'",(owner,propertyNam,estVal))
	conn.commit()
	curs.close()
	conn.close()

def deleteProperty(aadhar):
	conn = sqlite3.connect(propertyTable + ".sqlite")
	curs = conn.cursor()
	id = "property"
	curs.execute("delete from " + id + " where aadhar = '"+aadhar+"'")
	conn.commit()
	curs.close()
	conn.close()

def getPropertyTable():
	conn = sqlite3.connect(propertyTable + ".sqlite")
	curs = conn.cursor()
	id = "property"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows

####            Vehicle Table	  ####
def createVehicleTable():
	conn = sqlite3.connect(vehicleTable + ".sqlite")
	curs = conn.cursor()
	id = "vehicle"
	curs.execute("create table if not exists " + id + "(aadhar TEXT PRIMARY KEY, owner TEXT, vehicleName Text, estimateVal TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addVehicle(aadhar,owner,vehicleNam, estVal):
	conn = sqlite3.connect(vehicleTable + ".sqlite")
	curs = conn.cursor()
	id = "vehicle"
	curs.execute("insert into "+ id +" values(?,?,?,?)",(aadhar,owner,vehicleNam,estVal))
	conn.commit()
	curs.close()
	conn.close()

def updateVehicle(aadhar,owner,vehicleNam, estVal):
	conn = sqlite3.connect(vehicleTable + ".sqlite")
	curs = conn.cursor()
	id = "vehicle"
	curs.execute("update " + id + " set owner = ?, vehicleName = ?, estimateValue = ? where aadhar = '"+aadhar+"'",(owner,vehicleNam,estVal))
	conn.commit()
	curs.close()
	conn.close()

def deleteVehicle(aadhar):
	conn = sqlite3.connect(vehicleTable + ".sqlite")
	curs = conn.cursor()
	id = "vehicle"
	curs.execute("delete from " + id + " where aadhar = '"+aadhar+"'")
	conn.commit()
	curs.close()
	conn.close()
	
def getVehicleTable():
	conn = sqlite3.connect(vehicleTable + ".sqlite")
	curs = conn.cursor()
	id = "vehicle"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows



####            Bank Table	  ####
def createBankTable():
	conn = sqlite3.connect(bankTable + ".sqlite")
	curs = conn.cursor()
	id = "bank"
	curs.execute("create table if not exists " + id + "(aadhar TEXT PRIMARY KEY, balance TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def addPersonBalance(aadhar,bal):
	conn = sqlite3.connect(bankTable + ".sqlite")
	curs = conn.cursor()
	id = "bank"
	curs.execute("insert into "+ id +" values(?,?)",(aadhar,bal))
	conn.commit()
	curs.close()
	conn.close()

def updateBalance(aadhar,bal):
	conn = sqlite3.connect(bankTable + ".sqlite")
	curs = conn.cursor()
	id = "bank"
	curs.execute("update " + id + " set balance = ? where aadhar = '"+aadhar+"'",(bal))
	conn.commit()
	curs.close()
	conn.close()

def deleteBalance(aadhar):
	conn = sqlite3.connect(bankTable + ".sqlite")
	curs = conn.cursor()
	id = "bank"
	curs.execute("delete from " + id + " where aadhar = '"+aadhar+"'")
	conn.commit()
	curs.close()
	conn.close()

def getBankTable():
	conn = sqlite3.connect(bankTable + ".sqlite")
	curs = conn.cursor()
	id = "bank"
	curs.execute("select * from " + id)
	rows = curs.fetchall()
	conn.commit()
	curs.close()
	conn.close()
	return rows





#### calculation for defaulters
def getDefaultersList():
	conn = sqlite3.connect(salaryTable + ".sqlite")
	curs = conn.cursor()
	id = "salary"
	#curs.execute("select s.aadhar,name, (s.salary*12 - (p.estimateVal+v.estimateVal))-35000 from salary as s, property as p, vehicle as v where s.aadhar=p.aadhar and p.aadhar=v.aadhar and (s.salary*12 - (p.estimateVal+v.estimateVal))>35000")
	curs.execute("select s.aadhar,name, (s.salary*12-p.estimateVal+v.estimateVal) from salary as s,property as p,vehicle as v where s.aadhar = p.aadhar and p.aadhar = v.aadhar and (s.salary*12-p.estimateVal+v.estimateVal)>350000 group by s.aadhar")
	rows = curs.fetchall()
	print(rows)
	conn.commit()
	curs.close()
	conn.close()
	return rows






#############################

def createItemsDB(id):
	conn = sqlite3.connect(ItemsDB+".sqlite")
	#curs.execute("create table if not exists " + id + "(aadhar TEXT PRIMARY KEY, name TEXT, address Text,mobile TEXT)")

	curs = conn.cursor()
	id = "u"+id
	curs.execute("create table if not exists "+id+"(itemname TEXT PRIMARY KEY,quantity TEXT,notes TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def insertItems(id,itemname,quantity,notes):
	conn = sqlite3.connect(ItemsDB + ".sqlite")
	curs = conn.cursor()
	id = "u"+id
	curs.execute("insert into "+id+" values(?,?,?)",(itemname,quantity,notes))
	conn.commit()
	curs.close()
	conn.close()

def updateItem(id,itemname,quantity,notes):
	conn = sqlite3.connect(ItemsDB + ".sqlite")
	curs = conn.cursor()
	id = "u"+id
	curs.execute("update " + id + " set quantity = ?, notes = ? where itemname = '"+itemname+"'",(quantity,notes))
	conn.commit()
	curs.close()
	conn.close()

def deleteItem(id,itemname):
	conn = sqlite3.connect(ItemsDB + ".sqlite")
	curs = conn.cursor()
	id = "u"+id
	curs.execute("delete from " + id + " where itemname = '"+itemname+"'")
	conn.commit()
	curs.close()
	conn.close()

def createUsersDB():
	conn = sqlite3.connect(UsersDB+".sqlite")
	curs = conn.cursor()
	curs.execute("create table if not exists "+usersTable+"(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,password TEXT)")
	conn.commit()
	curs.close()
	conn.close()

def insertUsers(name,email,pwd):
	conn = sqlite3.connect(UsersDB + ".sqlite")
	curs = conn.cursor()
	curs.execute("insert into "+usersTable+" values(?,?,?,?)",(None,name,email,pwd))
	conn.commit()
	curs.close()
	conn.close()

def getUsers():
	conn = sqlite3.connect(UsersDB + ".sqlite")
	curs = conn.cursor()
	curs.execute("select * from "+usersTable)
	rows = curs.fetchall()
	curs.close()
	conn.close()
	return rows

def getItems(uid):
	uid = "u" + str(uid)
	conn = sqlite3.connect(ItemsDB + ".sqlite")
	curs = conn.cursor()
	curs.execute("select * from "+uid)
	rows = curs.fetchall()
	curs.close()
	conn.close()
	return rows


createUsersDB()

createAdminsTable()
createBankTable()
createPropertyTable()
createSalaryTable()
createVehicleTable()
createAdminstTable()
createManagersTable()
createFeedbacksTable()
#calculate12MSal()