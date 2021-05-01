from flask import Flask, redirect, url_for, request, render_template
from flask_apscheduler import APScheduler
from time import sleep
import sqlite3
app = Flask(__name__)
@app.route("/")
def home_page():
   return render_template("userinput.html")

@app.route('/tasklist',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

      conn = sqlite3.connect('./static/data/responses.db')
      curs = conn.cursor()

if __name__ == '__main__':
   app.run(debug = True)