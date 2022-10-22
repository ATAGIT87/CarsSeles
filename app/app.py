from typing import List, Dict
from flask import Flask, render_template, request, redirect
import mysql.connector
import json

carsales = Flask(__name__,template_folder='templates')


def db_connection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'carinfo'
    }
    connection = mysql.connector.connect(**config)
    return connection




@carsales.route('/', methods = ['GET','POST'])
def index():
    pr = []
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute(" select c.id as carid,o.id,o.name,o.address,o.car_id,o.insu_id,i.des,c.name,c.year,c.price from carinfo.owns o, carinfo.car c, carinfo.insurance i where o.car_id=c.id and o.insu_id=i.id;")
    for row in cursor.fetchall():
        pr.append({"idcar": row[0],"id": row[1],"name": row[2], "address": row[3],"carid": row[4],"insuid": row[5], "des": row[6], "carname": row[7], "year": row[8], "price": row[9]})
    connection.close()    
    return render_template("carslist.html", pr = pr)


@carsales.route("/addcar", methods = ['GET','POST'])
def addcar():
    connection = db_connection()
    if request.method == 'GET':
        return render_template("addcar.html", car = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        # conn = connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO car (id, name, year, price) VALUES (%s, %s, %s, %s)", (id, name, year, price) )
        connection.commit()
        connection.close()
        return redirect('/')


@carsales.route("/")
def carlist():
    carslist = []
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute(" select id, name, year, price from carinfo.car;")
    for row in cursor.fetchall():
        carslist.append({"id": row[0],"name": row[1], "year": row[2], "price": row[3]})
    connection.close()
    return render_template("carslist.html",carslist = carslist)



@carsales.route("/addinsu", methods = ['GET','POST'])
def addinsu():
     connection = db_connection()
     if request.method == 'GET':
         return render_template("addinsu.html", insu = {})
     if request.method == 'POST':
        id = int(request.form["id"])
        des = str(request.form["des"])
        cursor = connection.cursor()
        cursor.execute("INSERT INTO insurance (id, des) VALUES (%s, %s)", (int(id), str(des)) )
        connection.commit()
        connection.close()
        return redirect('/')



@carsales.route("/addperson", methods = ['GET','POST'])
def addperson():
    connection = db_connection()
    if request.method == 'GET':
        return render_template("addperson.html", pr = {})
    if request.method == 'POST':
        id = int(request.form["idp"])
        name = request.form["name"]
        address = request.form["address"]
        insu = int(request.form["insu"])
        car = int(request.form["car"])
        cursor = connection.cursor()
        cursor.execute("INSERT INTO owns (id,name,address,car_id,insu_id) VALUES (%s, %s,%s,%s,%s)", (id, name,address,car,insu) )
        connection.commit()
        connection.close()
        return redirect('/')        

@carsales.route('/deletecar/<int:idcar>')
def deletecar(idcar):
    connection = db_connection()
    cursor = connection.cursor()
    sql=("DELETE FROM owns WHERE id= %s") 
    cursor.execute(sql, (idcar,))
    connection.commit()
    connection.close()
    return redirect('/')



@carsales.route('/editperson/<int:idcar>',methods = ['GET','POST'])
def editperson(idcar):
    print('Hereeeeeeeeeeeeeee root')
    pr = []
    connection = db_connection()
    cursor = connection.cursor()
    if request.method == 'GET':
        print('Hereeeeeeeeeeeeeee get')
        cursor.execute("SELECT * FROM carinfo.owns")
        for row in cursor.fetchall():
            pr.append({"id": row[0], "name": row[1], "address": row[2], "carid": row[3],"insu_id": row[4]})
        connection.close()
        return render_template("addperson.html", pr = {})
    if request.method == 'POST':
        print('Hereeeeeeeeeeeeeee')


        name = str(request.form["name"])
        address = str(request.form["address"])
        #car = int(request.form["carid"])
        #insurance = int(request.form["insu_id"])
        sql=("UPDATE carinfo.owns SET name = %s, address = %s WHERE id =%s")
        cursor.execute(sql, (name, address, idcar))
        connection.commit()
        connection.close()
        return redirect('/')   


@carsales.route('/updatecar/<int:idcar>',methods = ['GET','POST'])
def updatecar(idcar):
    cr = []
    connection = db_connection()
    cursor = connection.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM car WHERE id= %s", (idcar,))
        for row in cursor.fetchall():
            cr.append({"idcar": row[0], "name": row[1], "year": row[2], "price": row[3]})
        connection.close()
        return render_template("addcar.html", car = {})
    if request.method == 'POST':
        name = str(request.form["name"])
        year = int(request.form["year"])
        price = float(request.form["price"])
        cursor = connection.cursor()
        sql=("UPDATE carinfo.car SET name = %s, year = %s, price = %s WHERE id = %s")
        cursor.execute(sql, (name, year, price, idcar))
        connection.commit()
        connection.close()
        return redirect('/')
             



if __name__ == '__main__':
    carsales.run(host='0.0.0.0')
