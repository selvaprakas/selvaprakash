import os
from flask import Flask,render_template,request,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///selva.db'
app.config['SECRET_KEY'] = 'Selva1999'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'

db = SQLAlchemy()



class Data(db.Model):
    SINo=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.DateTime,default=datetime.utcnow)
    Movement_Id= db.Column(db.String())
    Prodect_Id= db.Column(db.String())
    quantity= db.Column(db.String())
    From_Location=db.Column(db.String())
    To_Location=db.Column(db.String())
    
    def __init__(self,SINo,Movement_Id,Prodect_Id,quantity,From_Location,To_Location):
        self.SINo=SINo
        self.Movement_Id=Movement_Id
        self.Prodect_Id=Prodect_Id
        self.quantity=quantity
        self.From_Location=From_Location
        self.To_Location=To_Location

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/insert',methods = ['POST'])
def insert():
    if request.method == 'POST':
        SINo = request.form['SINo']
        Movement_Id = request.form['Movement_Id']
        Prodect_Id = request.form['Prodect_Id']
        quantity = request.form['quantity']
        From_Location = request.form['From_Location']
        To_Location = request.form['To_Location']

        my_data = Data(SINo,Movement_Id,Prodect_Id,quantity,From_Location,To_Location)
        db.session.add(my_data)
        db.session.commit()

        flash("product inserted Sucessfully")

        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('SINo'))

        my_data.SINo = request.form['SINo']
        my_data.Movement_Id = request.form['Movement_Id']
        my_data.Prodect_Id = request.form['Prodect_Id']
        my_data.quantity = request.form['quantity']
        my_data.From_Location = request.form['From_Location']
        my_data.To_Location = request.form['To_Location']

        db.session.commit()
        flash("product Updated Successfully")

        return redirect(url_for('Index'))
@app.route('/delete/<SINo>',methods = ['GET','POST'])
def delete(SINo):
    my_data = Data.query.get(SINo)
    db.session.delete(my_data)
    db.session.commit()

    flash("product Deleted Successfully")

    return redirect(url_for("Index"))

if __name__  == "__main__":
    app.run(debug=True)
