from flask import Flask, redirect, url_for, request, render_template
from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
app = Flask(__name__)
sense = SenseHat()
@app.route("/")
def home_page():
   return render_template("login.html")


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
   sense.show_message("Welcome " + name)
   return "Welcome %s" % name
# Lines 22 to 25 is where the SenseHat is supposed to display the user input text, but I haven't finished it yet as we got pulled from breakout rooms.



if __name__ == '__main__':
   app.run(debug = True)