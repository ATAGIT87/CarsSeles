create database IF NOT EXISTS carinfo;
use carinfo;

CREATE TABLE IF NOT EXISTS carinfo.car (id int(11) NOT NULL AUTO_INCREMENT, name varchar(100) NOT NULL, year varchar(20) NOT NULL,price varchar(20) DEFAULT NULL,PRIMARY KEY (id));

insert into carinfo.car (id,name,year,price) SELECT 1,'BMW','2020','20000' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM carinfo.car);

CREATE TABLE IF NOT EXISTS carinfo.insurance (id int(11) NOT NULL AUTO_INCREMENT,des varchar(100) NOT NULL, PRIMARY KEY (id));

insert into carinfo.insurance (id,des) SELECT 1,'AXA' FROM DUAL  WHERE NOT EXISTS (SELECT * FROM carinfo.insurance);

CREATE TABLE IF NOT EXISTS carinfo.owns (id int(11) NOT NULL AUTO_INCREMENT,name varchar(100) NOT NULL, address varchar(100) NULL,car_id int(11) NOT NULL,insu_id int(11) NOT NULL,PRIMARY KEY (id),   CONSTRAINT fk_owns_car FOREIGN KEY (car_id) REFERENCES carinfo.car (id),CONSTRAINT fk_owns_insu FOREIGN KEY (insu_id) REFERENCES insurance (id));

insert into carinfo.owns (id,name,address,car_id,insu_id) SELECT 1,'Ali Taba','Kiel',1,1 FROM DUAL  WHERE NOT EXISTS (SELECT * FROM carinfo.owns);