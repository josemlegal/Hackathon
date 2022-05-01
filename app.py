from flask import Flask, request, flash, redirect, render_template, url_for
import requests 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)



@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/entrada')
def entrada():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

app.run(host="137.184.32.228", port=80)     

if __name__ == "__main__":
    app.run(debug=True)
