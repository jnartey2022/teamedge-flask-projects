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
   sense.show_message("Welcome " + name, text_colour=[0,255,0])
   color = (0, 255, 0)
   return "Welcome %s" % name

# Lines 20 to 23, this portion of the code is where the text from the website displays onto the SenseHat.



if __name__ == '__main__':
   app.run(debug = True)