from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os
import webbrowser
import re
import pymysql


app = Flask(__name__)

def __init__(self):
        try:
            #Crea una conexion con los datos que se recolectaron de XAMPP
            self.conn = pymysql.connect(host='localhost', user="root", passwd='', port="3306", db="pec")
            self.cursor = self.conn.cursor()

        except pymysql.Error as err:
            self.conn = pymysql.connect(host='localhost', user="root", passwd='', port="3306")
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS pec")
            self.cursor.execute("USE pec")
            print("\nCreación exitosa\n")
        

def crearTabladonadores(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `donadores` (`iddonador` int(11) NOT NULL AUTO_INCREMENT,`nombre` varchar(50) NOT NULL,`apellido` varchar(50) NOT NULL,`email` varchar(50) NOT NULL,`telefono` varchar(15) NOT NULL,`pago` varchar(30) NOT NULL,`comentarios` varchar(500) NOT NULL;")

def conectar(self):
        try:
            self.crearTabladonadores()
        except pymysql.Error as err: 
            print ("\nError al intentar la conexión: {0}".format(err))



@app.route('/')
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
