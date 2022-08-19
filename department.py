from app import app, Department, db
from flask import request, render_template, redirect

@app.route('/department', methods=['GET', 'POST'])
def dep():
  if request.method == 'POST':
    name = request.form['name']
    newDepartment = Department(name=name)
    db.session.add(newDepartment)
    db.session.commit()
  headings = ("Id", "Name")
  department = Department.query.order_by(Department.id).all()
  return render_template('department.html', headings=headings, data = department)



@app.route('/department/create')
def depCreate():
  return render_template('create_department.html')

@app.route('/department/update/<id>', methods=['GET', 'POST'])
def depUpdate(id):
  if request.method == 'POST':
    department = Department.query.get(id)
    department.name = request.form['name']
    db.session.commit()
    return redirect('/department')
  department = Department.query.get(id)
  return render_template('update_department.html', department=department)

@app.route('/department/delete/<id>')
def depDelete(id):
  department = Department.query.get(id)
  db.session.delete(department)
  db.session.commit()
  return redirect('/department')