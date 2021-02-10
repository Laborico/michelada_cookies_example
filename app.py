

import datetime

from flask import Flask, render_template, make_response, request, redirect, session, flash


app = Flask(__name__)
app.secret_key = 'Z9GP$75[q-sf9Fi=.!>r$X"sYlTzZ"vZP8_#b<Bt~nFG?%klFe=|l?p"k|2$;9*'


@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      if email != '' and password !='':
         return redirect(f'/backoffice?email={email}&password={password}')

   return render_template("login.html"), 200


@app.route('/backoffice')
def backoffice(methods=['GET']):

   email=request.args.get('email', type= str)
   password=request.args.get('password', type= str)

   if len(email)>0 and len(password)>0:
      Info_de_user={
         'email':email,
         'password':password
      }
      return render_template("backoffice.html",Info_de_user=Info_de_user), 200
   else:
      flash('Primero debes de iniciar sesion')
      return redirect(f'/login')

@app.route('/logout')
def logout():  
    return redirect('/login')

@app.route('/')
def home():
    return redirect(f'/login')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8080)

