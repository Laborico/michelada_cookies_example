

import datetime

from flask import Flask, render_template, make_response, request, redirect, session


app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "hD4GbkeacT3KXuwZ"


@app.route('/login', methods=['GET', 'POST'])
def login():
   """
   Home
   :return:
   :rtype:
   """
   if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      if email != '' and password !='':
         session['email']=email
         return redirect(f'/backoffice')

   return render_template("login.html"), 200


@app.route('/backoffice')
def backoffice(methods=['GET']):
   return render_template("backoffice.html"), 200


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8080)

