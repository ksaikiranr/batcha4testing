from flask import *
from forms import *
from dbAccess import *
from flask_mail import Message, Mail
import datetime

mail = Mail()

itemsList = []
app = Flask(__name__)

app.secret_key = "development-key"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'ksaikirancse.rymec@gmail.com'
app.config["MAIL_PASSWORD"] = 'osksaikiran'

mail.init_app(app)
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form=form)
		else:
			dateTime = datetime.datetime.now()
			addFeedback(form.senderEmail.data,form.senderName.data,form.emailSubject.data,form.emailMessage.data, str(dateTime))
			#msg = Message(form.emailSubject.data, sender='ksaikirancse.rymec@gmail.com', recipients=['ksaikirancse.rymec@gmail.com'])
			#msg.body = """From: %s &lt;%s&gt;%s""" % (form.senderName.data, form.senderEmail.data, form.emailMessage.data)
			#mail.send(msg)
			
			return redirect(url_for('index'))
	
	elif request.method == 'GET':
		return render_template('contact.html', form=form)
	
@app.route("/signup", methods=['GET','POST'])
def signup():
	if 'email' in session:
		return redirect(url_for('home'))
	form = SignupForm()

	if request.method == "POST":
		if form.validate() == False:
			return render_template("signup.html",form = form)
		else:
			if form.loginType.data == 'Users':
				addAdmin(form.email.data, form.name.data, form.password.data)
				rows = getAdmins()
			elif form.loginType.data == 'Manager':
				addManager(form.email.data, form.name.data, form.password.data)
				rows = getManagers()
			else:
				addAdminst(form.email.data, form.name.data, form.password.data)
				rows = getAdminst()
			for row in rows:
				print(form.email.data)
				print(row[2])
				print(form.password.data)
				print(row[3] + "\n")
				if row[1] == form.email.data and row[3] == form.password.data:
					session['email'] = form.email.data
					session['name'] = row[2]
					session['id'] = row[0]
					session['loginType'] = form.loginType.data
					return redirect(url_for('home',user = (session['id'],session['name'],session['email'],session['loginType'])))
	elif request.method == "GET":
		return render_template("signup.html", form = form)

@app.route("/login", methods=['GET','POST'])
def login():
	if 'email' in session:
		return redirect(url_for('home',user=(session['id'],session['name'],session['email'],session['loginType'])))
	form = LoginForm()

	if request.method == "POST":
		if form.validate() == False:
			return render_template("login.html",form = form)
		else:
			if form.loginType.data == 'Users':
				rows = getAdmins()
			elif form.loginType.data == 'Manager':
				rows = getManagers()
			else:
				rows = getAdminst()
			for row in rows:
				print(form.email.data)
				print(row[2])
				print(form.password.data)
				print(row[3]+"\n")
				if row[1] == form.email.data and row[3] == form.password.data:
					session['email'] = form.email.data
					session['name'] = row[2]
					session['id'] = row[0]
					session['loginType'] = form.loginType.data
					return redirect(url_for('home'))
			else:
				return redirect(url_for('login'))

	elif request.method == "GET":
		return render_template("login.html", form = form)

@app.route("/logout")
def logout():
	session.pop('email',None)
	session.pop('name',None)
	session.pop('id',None)
	session.pop('loginType', None)
	return redirect(url_for('login'))

@app.route("/home", methods=['GET','POST'])
def home():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect( url_for('login'))
		#itemsList = getItems(session['id'])
		salaryList = getSalaryTable()
		vehicleList = getVehicleTable()
		print(vehicleList)
		bankList = getBankTable()
		propertyList = getPropertyTable()
		adminList = getManagers()
		defaultersList = getDefaultersList()
		feedbacks = getFeedbacks()
		return render_template("home.html",defaultersList = defaultersList,adminList = adminList, salaryList=salaryList,vehicleList = vehicleList,bankList=bankList,propertyList=propertyList, feedbacksList = feedbacks)

@app.route("/addperson",methods=['GET','POST'])
def addperson():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect( url_for('login'))
	form = PersonForm()
	if request.method == "GET":
		return render_template("addperson.html",form =form)
	elif request.method == "POST":
		if form.validate() == False:
			return render_template("addperson.html",form = form)
		
		addPersonSalary(form.aadhar.data,form.name.data,form.salary.data)
		#insertItems(str(session['id']),form.itemname.data,form.quantity.data,form.notes.data)
		return redirect(url_for('home'))


@app.route("/removeperson", methods=['GET', 'POST'])
def removeperson():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect(url_for('login'))
	form = RemovePersonForm()
	if request.method == "GET":
		return render_template("removeperson.html", form=form)
	elif request.method == "POST":
		if form.validate() == False:
			return render_template("removeperson.html", form=form)
		deletePerson(form.removeid.data)
		return redirect(url_for('home'))



@app.route("/addproperty", methods=['GET', 'POST'])
def addproperty():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect(url_for('login'))
	print(request)
	form = PropertyForm()
	if request.method == "GET":
		return render_template("addproperty.html", form=form)
	elif request.method == "POST":
		if form.validate() == False:
			return render_template("addproperty.html", form=form)
		
		addProperty(form.aadhar.data,form.owner.data,form.pname.data,form.estimatedvalue.data)
		return redirect(url_for('home'))


@app.route("/removeproperty", methods=['GET', 'POST'])
def removeproperty():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect(url_for('login'))
	form = RemovePropertyForm()
	if request.method == "GET":
		return render_template("removeproperty.html", form=form)
	elif request.method == "POST":
		if form.validate() == False:
			return render_template("removeproperty.html", form=form)
		deleteProperty(form.removeid.data)
		return redirect(url_for('home'))


@app.route("/addvehicle", methods=['GET', 'POST'])
def addvehicle():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect(url_for('login'))
	form = VehicleForm()
	if request.method == "GET":
		return render_template("addvehicle.html", form=form)
	elif request.method == "POST":
		if form.validate() == False:
			return render_template("addvehicle.html", form=form)
			
		addVehicle(form.aadhar.data, form.owner.data, form.vname.data, form.estimatedvalue.data)
		return redirect(url_for('home'))


@app.route("/removevehicle", methods=['GET', 'POST'])
def removevehicle():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect(url_for('login'))
	form = RemoveVehicleForm()
	if request.method == "GET":
		return render_template("removevehicle.html", form=form)
	elif request.method == "POST":
		if form.validate() == False:
			return render_template("removevehicle.html", form=form)
		deleteVehicle(form.removeid.data)
		return redirect(url_for('home'))





@app.route("/edititem",methods=['GET','POST'])
def edititem():
	if request.method == 'GET':
		if 'email' not in session:
			return redirect( url_for('login'))
	form = ItemForm()
	if request.method == "GET":
		print("==========================IN get req===========================")
		print(form.itemname.data)
		return render_template("edititem.html",form =form)
	elif request.method == "POST":
		print("==========================IN post req===========================")
		if 'edit' in request.form:
			if form.validate() == False:
				return render_template("edititem.html",form = form)
			updateItem(str(session['id']),form.itemname.data,form.quantity.data,form.notes.data)
			return redirect(url_for('home'))
		else:
			print(request.form)
			print(list(request.form))
			req = list(request.form)
			print(req)
			delC = req[0]
			if delC.startswith('de###'):
				print("called delete===========")
				itemname = delC.split('$')
				deleteItem(str(session['id']),itemname[1])
				return redirect(url_for('home'))
			req = req[0]
			req = req.split('$')
			print(req)
			form.itemname.data = req[0]
			form.quantity.data = req[1]
			form.notes.data = req[2]
			return render_template("edititem.html",form =form)

if __name__ == "__main__":
	app.run(debug=True)
