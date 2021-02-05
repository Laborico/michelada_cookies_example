

import datetime

from flask import Flask, render_template, make_response, request, redirect, session, flash


app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=1)
app.secret_key = 'Z9GP$75[q-sf9Fi=.!>r$X"sYlTzZ"vZP8_#b<Bt~nFG?%klFe=|l?p"k|2$;9*'


@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      if email != '' and password !='':
         session['email']=email
         session['password']=password
         return redirect(f'/backoffice')

   return render_template("login.html"), 200


@app.route('/backoffice')
def backoffice(methods=['GET']):
   if 'email' in session:
      return render_template("backoffice.html",info={'email':session['email'],'password':session['password']}), 200
   else:
      flash('Primero debes de iniciar sesion')
      return redirect(f'/login')

@app.route('/logout')
def logout():
    session.pop('email')         
    session.pop('password')         
    return redirect('/login')

@app.route('/')
def home():
    return redirect(f'/backoffice')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8080)

