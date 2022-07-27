
from flask import Flask , request , render_template , redirect
from flask_pymongo import pymongo
#from bson import json_util
#import json
import pymongo

app = Flask( __name__ ) 
client = pymongo.MongoClient('localhost:27017')
db = client['db']
employee = db['employee']


@app.route("/" , methods=['GET','POST'])
def myhome():
    if request.method=='POST':
        x = request.form['emp_name']
        y = request.form['emp_age']
        z = request.form["emp_email"]
        print(x,y,z)
        db.employee.insert_one({'name':x , 'age':int(y) , 'email': z})
    return render_template("home.html")

@app.route("/get_data" , methods=['GET'])
def login():
    employee = db.employee.find()
    employee = list(employee)
    return render_template('list.html' , employee=employee)




@app.route("/replace_employee/<string:name>-<string:email>" , methods=['GET','POST'])
def replace_employee(name,email):
    if request.method=='POST':
        x = request.form['emp_name']
        y = request.form['emp_age']
        z = request.form["emp_email"]
        db.employee.replace_one({'name': name ,'email': email}, {'name': x, 'age': int(y) , 'email': z})
        return redirect("/get_data")
    return render_template("update.html")

@app.route("/delete_employee/<string:name>-<string:email>" , methods=['GET','POST'])
def delete_employee(name,email):
    db.employee.delete_one({'name':name,  'email':email})
    return redirect("/get_data")
if __name__ =='__main__':
    app.run( host='0.0.0.0',port=9000)