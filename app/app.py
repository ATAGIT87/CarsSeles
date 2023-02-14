from typing import List, Dict
from flask import Flask, render_template, request, redirect,jsonify
import mysql.connector

carsales = Flask(__name__)   

def db_connection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'test'
    }
    connection = mysql.connector.connect(**config)
    return connection
 

@carsales.route('/')
def index():
    
    return render_template('index.html')
 
@carsales.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
     connection = db_connection()
     cursor = connection.cursor()
     person = []
     print('hiier ist ajax')
     if request.method == 'POST':
        search_word = request.form['query']
     if search_word == '':
            query = " select p.id,p.name,p.address,c.id,c.name,c.year,c.price,h.address,b.color,b.engine,j.titel from persons p, cars c,houses h, boats b, jobs j where p.car_id=c.id and p.house_id=h.id and p.boat_id=b.id and p.job_id=j.id ORDER BY p.name"
            cursor.execute(query)
            person= cursor.fetchall()
     else:    
            query = "select p.id,p.name,p.address,c.id,c.name,c.year,c.price,h.address,b.color,b.engine,j.titel from persons p, cars c,houses h, boats b, jobs j where p.car_id=c.id and p.house_id=h.id and p.boat_id=b.id and p.job_id=j.id and (p.name LIKE '%{}%' OR c.year LIKE '%{}%' OR c.price LIKE '%{}%') ORDER BY p.name DESC LIMIT 20".format(search_word,search_word,search_word)
            cursor.execute(query)
            person= cursor.fetchall()
     return jsonify({'htmlresponse': render_template('response.html', person=person)})



@carsales.route("/selectcars",methods=["POST","GET"])
def selectcars():
     connection = db_connection()
     cur = connection.cursor()
     cars = []
     print('hiier ist select cars')
     search_word = request.form['id'] 
     qu  = "select c.id,c.name,c.year,c.price,i.id,i.des from cars c,insurance i where c.insu_id=i.id and c.id={}".format(search_word)
     cur.execute(qu)
     cars= cur.fetchall()
     return render_template('index.html',cars=cars)

if __name__ == '__main__':
    carsales.run(host='0.0.0.0')
