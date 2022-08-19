from app import app, Employee, Department, db
from flask import request, render_template, redirect


@app.route('/employee', methods=['GET', 'POST'])
def func():
  if request.method == 'POST':
    name = request.form['name']
    title = request.form['title']
    department = request.form['department']
    years_of_exp = request.form['years_of_exp']
    salary = request.form['salary']
    department_id = Department.query.filter(Department.name==department).one().id
    newEmployee = Employee(name=name,title=title,department_id=department_id,years_of_exp=years_of_exp,salary=salary)
    db.session.add(newEmployee)
    db.session.commit()
    return redirect('/employee')

  headings = ("Id", "Name", "Title", "Department", "Years of Experience", "Salary")
  result = db.session.query(Employee, Department).join(Department).order_by(Employee.id).all()
  return render_template('employee.html', headings=headings, data = result)

@app.route('/employee/create')
def create():
  department = Department.query.order_by(Department.id).all()
  return render_template('create_employee.html', department=department)


@app.route('/employee/update/<id>', methods=['GET', 'POST'])
def update(id):
  if request.method == 'POST':
    employee = Employee.query.get(id)
    print(employee.name)
    employee.name = request.form['name']
    employee.title = request.form['title']
    department = request.form['department']
    employee.years_of_exp = request.form['years_of_exp']
    employee.salary = request.form['salary']
    employee.department_id = Department.query.filter(Department.name==department).one().id
    db.session.commit()
    return redirect('/employee')
  employee = Employee.query.get(id)
  department = Department.query.order_by(Department.id).all()
  employeeDep = Department.query.get(employee.department_id)
  return render_template('update_employee.html', employee=employee, department= department, employeeDep = employeeDep.name)

@app.route('/employee/delete/<id>')
def delete(id):
  employee = Employee.query.get(id)
  db.session.delete(employee)
  db.session.commit()
  return redirect('/employee')