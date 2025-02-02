from flask import Flask, request, flash, url_for, redirect, render_template  
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'  
app.config['SECRET_KEY'] = "secret key"  
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  
  
class Employees(db.Model):
   __tablename__ = 'employees'
   id = db.Column(db.Integer, primary_key = True)  
   name = db.Column(db.String(100))  
   salary = db.Column(db.Float(50))  
   age = db.Column(db.Integer)   
   pin = db.Column(db.String(10))  
  
   def __init__(self, name, salary, age, pin):  
      self.name = name  
      self.salary = salary  
      self.age = age  
      self.pin = pin  
 
@app.route('/')  
def list_employees():
   return render_template('list_employees.html', Employees=Employees.query.all())  
 
@app.route('/add', methods=['GET', 'POST'])  
def addEmployee():  
   if request.method=='POST':  
      if not request.form['name'] or not request.form['salary'] or not request.form['age']:  
         flash('Please enter all the fields', 'error')  
      else:  
         employee=Employees(request.form['name'], request.form['salary'], request.form['age'], request.form['pin'])
         db.session.add(employee)  
         db.session.commit()  
         flash('Record was successfully added')  
         return redirect(url_for('list_employees'))  
   return render_template('add.html')  
  
if __name__ == '__main__':  
   db.create_all()  
   app.run(debug=True)