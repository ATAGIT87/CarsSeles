from flask import Flask, render_template, request, redirect
import mariadb
import sys

carsales = Flask(__name__)

def connection():
    conn = mariadb.connect(
        user="root", #Your login user
        password="Password123!", #Your login password
        host="127.0.0.1", #Your server name 
        port=3306,
        database="CarSeles")
    return conn
	

@carsales.route("/")
def main():
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(" select p.name,p.address,i.des,c.name,c.year,c.price from CarSeles.TblPersons p, CarSeles.TblCars c, CarSeles.TblInsurance i where p.Car_ID=c.ID and p.Insurance_Id=i.ID;")
    for row in cursor.fetchall():
        cars.append({"name": row[0], "address": row[1], "des": row[2], "carname": row[3], "year": row[4], "price": row[5]})
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
        cursor.execute("INSERT INTO TblCars (id, name, year, price) VALUES (?, ?, ?, ?)", (id, name, year, price) )
        conn.commit()
        conn.close()
        return redirect('/')


@carsales.route("/addinsu", methods = ['GET','POST'])
def addinsu():
    if request.method == 'GET':
        return render_template("addinsu.html", insu = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        des = request.form["des"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblInsurance (id, des) VALUES (?, ?)", (id, des) )
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
        cursor.execute("INSERT INTO TblPersons (id,name,address,insurance_id,car_id) VALUES (?, ?,?,?,?)", (id, name,address,insu,car) )
        conn.commit()
        conn.close()
        return redirect('/')        

@carsales.route('/updatecar/<int:id>',methods = ['GET','POST'])
def updatecar(id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM TblCars WHERE id=?", (id,))
        for row in cursor.fetchall():
            cr.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
        conn.close()
        return render_template("addcar.html", car = cr[0])
    if request.method == 'POST':
        name = str(request.form["name"])
        year = int(request.form["year"])
        price = float(request.form["price"])
        cursor.execute("UPDATE TblCars SET name = ?, year = ?, price = ? WHERE id = ?", (name, year, price, id))
        conn.commit()
        conn.close()
        return redirect('/')

@carsales.route('/deletecar/<int:id>')
def deletecar(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TblCars WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if(__name__ == "__main__"):
    carsales.run()