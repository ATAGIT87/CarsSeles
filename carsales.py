from flask import Flask, render_template, request, redirect
# import mariadb
import pymysql
import sys

carsales = Flask(__name__)

def connection():
    conn = pymysql.connect(
        user="root", #Your login user
        password="Password123!", #Your login password
        host="127.0.0.1", #Your server name 
        port=3306,
        database="carinfo")
    return conn
	

@carsales.route("/")
def main():
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(" select c.id,o.id,o.name,o.address,i.des,c.name,c.year,c.price from carinfo.owns o, carinfo.car c, carinfo.insurance i where o.car_id=c.id and o.insu_id=i.id;")
    for row in cursor.fetchall():
        cars.append({"id": row[0],"idp": row[1],"name": row[2], "address": row[3], "des": row[4], "carname": row[5], "year": row[6], "price": row[7]})
    conn.close()    
    return render_template("carslist.html", cars = cars)



@carsales.route("/addcar", methods = ['GET','POST'])
def addcar():
    if request.method == 'GET':
        return render_template("addcar.html", car = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO car (id, name, year, price) VALUES (%s, %s, %s, %s)", (id, name, year, price) )
        conn.commit()
        conn.close()
        return redirect('/')


@carsales.route("/")
def carlist():
    carslist = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(" select id, name, year, price from carinfo.car;")
    for row in cursor.fetchall():
        carslist.append({"id": row[0],"name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    return render_template("carslist.html",carslist = carslist)



@carsales.route("/addinsu", methods = ['GET','POST'])
def addinsu():
    if request.method == 'GET':
        return render_template("addinsu.html", insu = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        des = str(request.form["des"])
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO insurance (id, des) VALUES (%s, %s)", (int(id), str(des)) )
        conn.commit()
        conn.close()
        return redirect('/')



@carsales.route("/addperson", methods = ['GET','POST'])
def addperson():
    if request.method == 'GET':
        return render_template("addperson.html", perso = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        address = request.form["address"]
        insu = int(request.form["insu"])
        car = int(request.form["car"])
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO owns (id,name,address,car_id,insu_id) VALUES (%s, %s,%s,%s,%s)", (id, name,address,car,insu) )
        conn.commit()
        conn.close()
        return redirect('/')        

@carsales.route('/deletecar/<int:id>')
def deletecar(id):
    conn = connection()
    cursor = conn.cursor()
    sql=("DELETE FROM owns WHERE id= %s") 
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()
    return redirect('/')


@carsales.route('/updatecar/<int:id>',methods = ['GET','POST'])
def updatecar(id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM car WHERE id= %s", (id,))
        for row in cursor.fetchall():
            cr.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
        conn.close()
        return render_template("addcar.html", car = {})
    if request.method == 'POST':
        name = str(request.form["name"])
        year = int(request.form["year"])
        price = float(request.form["price"])
        conn = connection()
        cursor = conn.cursor()
        sql=("UPDATE TblCars SET name = %s, year = %s, price = %s WHERE id = %s")
        cursor.execute(sql, (name, year, price, id))
        conn.commit()
        conn.close()
        return redirect('/')
        

@carsales.route('/updateperson/<int:idp>',methods = ['GET','POST'])
def editperson(idp):
    pr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM owns WHERE id=%s", (id,))
        for row in cursor.fetchall():
            pr.append({"idp": row[0], "name": row[1], "address": row[2], "car_id": row[3],"insu_id": row[4]})
        conn.close()
        return render_template("addperson.html", perso = {})
    if request.method == 'POST':
        name = str(request.form["name"])
        address = str(request.form["address"])
        car = int(request.form["car_id"])
        insurance = int(request.form["insu_id"])
        sql=("UPDATE carinfo.owns SET name = %s, address = %s, car_id = %s, insu_id = %s WHERE id = %s")
        cursor.execute(sql, (name, address, insurance, car, idp))
        conn.commit()
        conn.close()
        return redirect('/')        


if(__name__ == "__main__"):
    carsales.run()