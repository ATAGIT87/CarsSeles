from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql


class A:
    def a():

        # Open database connection ( If database is not created don't give dbname)
        db = pymysql.connect(
                user="root", #Your login user
                password="Password123!", #Your login password
                host="127.0.0.1", #Your server name 
                port=3306
               )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # For creating create db
        # Below line  is hide your warning 
        cursor.execute("SET sql_notes = 0; ")
        # create db here....
        cursor.execute("create database IF NOT EXISTS carinfo")



        # create table car
        cursor.execute("SET sql_notes = 0; ")
        cursor.execute("CREATE TABLE IF NOT EXISTS carinfo.car (id int(11) NOT NULL AUTO_INCREMENT, name varchar(100) NOT NULL, year varchar(20) NOT NULL,price varchar(20) DEFAULT NULL,PRIMARY KEY (id))")
        cursor.execute("SET sql_notes = 1; ")

        #insert data car
        cursor.execute("insert into carinfo.car (id,name,year,price) SELECT 1,'BMW','2020','20000' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM carinfo.car)")

        # Commit your changes in the database
        db.commit()

        # create table insurance
        cursor.execute("SET sql_notes = 0; ")
        cursor.execute("CREATE TABLE IF NOT EXISTS carinfo.insurance (id int(11) NOT NULL AUTO_INCREMENT,des varchar(100) NOT NULL, PRIMARY KEY (id))")
        cursor.execute("SET sql_notes = 1; ")

        #insert data insurance
        cursor.execute("insert into carinfo.insurance (id,des) SELECT 1,'AXA' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM carinfo.insurance)")

        # Commit your changes in the database
        db.commit()

        # create table owns
        cursor.execute("SET sql_notes = 0; ")
        cursor.execute("CREATE TABLE IF NOT EXISTS carinfo.owns (id int(11) NOT NULL AUTO_INCREMENT,name varchar(100) NOT NULL, address varchar(100) NULL,car_id int(11) "+
        "NOT NULL,insu_id int(11) NOT NULL,PRIMARY KEY (id),   CONSTRAINT fk_owns_car FOREIGN KEY (car_id) REFERENCES carinfo.car (id),CONSTRAINT fk_owns_insu FOREIGN KEY (insu_id) REFERENCES insurance (id));")
        cursor.execute("SET sql_notes = 1; ")

        #insert data owns
        cursor.execute("insert into carinfo.owns (id,name,address,car_id,insu_id) SELECT 1,'Ali Taba','Kiel',1,1 FROM DUAL  WHERE NOT EXISTS (SELECT * FROM carinfo.owns)")

        # Commit your changes in the database
        db.commit()
        db.close()

