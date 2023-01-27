create database IF NOT EXISTS test;
use test;

--create table insurances and insert sample data
CREATE TABLE IF NOT EXISTS test.insurance (id int(11) NOT NULL AUTO_INCREMENT,des varchar(100) NOT NULL, PRIMARY KEY (id));

insert into test.insurance (id,des) SELECT 1,'AXA' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM test.insurance);
insert into test.insurance (id,des) SELECT 2,'ADAC' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM test.insurance);

--create table cars and insert sample data
CREATE TABLE IF NOT EXISTS test.cars (id int(11) NOT NULL AUTO_INCREMENT, name varchar(100) NOT NULL, year varchar(20) NOT NULL,price varchar(20) DEFAULT NULL,insu_id int(11),PRIMARY KEY (id), CONSTRAINT fk_car_insu FOREIGN KEY (insu_id) REFERENCES test.insurance (id));

insert into test.cars (id,name,year,price,insu_id) SELECT 2,'BMW','2020','20000',1 FROM DUAL  WHERE NOT EXISTS (SELECT * FROM test.cars);

--create table house and insert sample data
CREATE TABLE IF NOT EXISTS test.houses (id int(11) NOT NULL AUTO_INCREMENT, address varchar(100) NOT NULL,PRIMARY KEY (id));

insert into test.houses (id,address) SELECT 1,'24109 Kiel Musster Strsse 123' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM test.houses);

--create table boats and insert sample data
CREATE TABLE IF NOT EXISTS test.boats (id int(11) NOT NULL AUTO_INCREMENT, color varchar(100) NOT NULL, engine varchar(100) NOT NULL,PRIMARY KEY (id));

insert into test.boats (id,color,engine) SELECT 1,'red','diesel' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM test.boats);

--create table jobs and insert sample data
CREATE TABLE IF NOT EXISTS test.jobs (id int(11) NOT NULL AUTO_INCREMENT, titel varchar(100) NOT NULL, PRIMARY KEY (id));

insert into test.jobs (id,titel) SELECT 1,'developer' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM test.jobs);

--create persons persons and insert sample data

CREATE TABLE IF NOT EXISTS test.persons (id int(11) NOT NULL AUTO_INCREMENT,name varchar(100) NOT NULL, address varchar(100) NULL,car_id int(11) NOT NULL,house_id int(11) NOT NULL,boat_id int(11) NOT NULL,job_id int(11) NOT NULL,PRIMARY KEY (id),   CONSTRAINT fk_perso_car FOREIGN KEY (car_id) REFERENCES test.cars (id),CONSTRAINT fk_perso_house FOREIGN KEY (house_id) REFERENCES test.houses (id),CONSTRAINT fk_perso_boats FOREIGN KEY (boat_id) REFERENCES test.boats (id),CONSTRAINT fk_perso_job FOREIGN KEY (job_id) REFERENCES test.jobs (id));

insert into test.persons (id,name,address,car_id,house_id,boat_id,job_id) SELECT 1,'Ali Taba','Kiel',2,1,1,1 FROM DUAL  WHERE NOT EXISTS (SELECT * FROM test.persons);