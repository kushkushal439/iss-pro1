from flask import Flask,render_template,request,redirect,url_for,flash
from werkzeug.security import check_password_hash, generate_password_hash
import json
import os
app = Flask(__name__)


@app.route('/' , methods=['GET','POST'])
def signUp():
   if request.method == 'POST':
      name = request.form['username']
      eMail=request.form['email']
      password=request.form['password']
      check =get_data(eMail)
      if check == None:
         save_to_form(name,eMail,password)
         return render_template('success.html')
      else:
         return render_template('failure.html')
   
   return render_template('register.html')



@app.route('/user/<user_id>')
def display(user_id):
  data = get_data(user_id)
  if data == None:
     return render_template('userDoesNotExist.html')
  else:
     return render_template('displayUser.html' , data=data)
  


def get_data(user_id):
    if not os.path.exists('users.txt'):
        return None
    with open('users.txt','r') as f:
         for line in f:
             data = json.loads(line)
             if data['email'] == user_id:
                return data
         f.close()
     
    return None

def save_to_form(name,eMail,password):
   data = {'name': name , 'email': eMail , 'password': generate_password_hash(password)}
   with open("users.txt",'a+') as f:
      json.dump(data,f)
      f.write('\n')
      f.close()



if __name__== '__main__':
    app.run(debug=True)


