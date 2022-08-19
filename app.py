from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:<Password>@localhost:5432/flaskdb'
db = SQLAlchemy(app)


class Department(db.Model):
  __tablename__ = 'Department'
  id = db.Column(db.Integer, primary_key=True)
  name =  db.Column(db.String(40))
  employee = db.relationship('Employee', backref='Department')

  def __init__(self, name):
    self.name = name

class Employee(db.Model):
  __tablename__ = 'Employee'
  id = db.Column(db.Integer, primary_key=True)
  name =  db.Column(db.String(40), nullable=False)
  title = db.Column(db.String(40), nullable=False)
  department_id = db.Column(db.Integer, db.ForeignKey('Department.id'))
  years_of_exp = db.Column(db.Integer, default=0)
  salary = db.Column(db.Integer, default=0)

  def ___init__(self, name, title, department_id, years_of_exp, salary):
    self.name = name
    self.title = title
    self.department_id = department_id
    self.years_of_exp = years_of_exp
    self.salary = salary

import department
import employee
  
@app.route('/')
def index():
  employee = Employee.query.order_by(Employee.id).all()
  print(employee[0].name)
  return render_template('base.html')


if __name__ == "__main__":
  app.run(debug=True)