from flask import Flask, redirect, url_for, request, render_template
from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
app = Flask(__name__)
@app.route("/")
def home_page():
   return render_template("login.html")

@app.route('/success/<name>')
def success(name):
   return "Welcome %s" %name + ". This is the SenseHat project"

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/success/<name>')
def success(name):
name = request.form['nm']
   return "


sense = SenseHat()
name = request.form['nm']
sense.show_message(name)

if __name__ == '__main__':
   app.run(debug = True)