# from flask import Flask, render_template, redirect, url_for, request
# import re
# data={}
# app = Flask(__name__)
# @app.route('/')
# def MainPage():
#     return render_template('mainPage.html')
#
# @app.route('/signin', methods=['GET', 'POST'])
# def login():
#     i=0
#     if request.method=="POST":
#             if data[request.form['username']] == request.form['password']:
#                 return 'pass'
#             else:
#                 return 'retry'
#     return render_template('index.html')
#
# @app.route('/signup',methods=['GET','POST'])
# def signup():
#     i=0
#     if request.method=='POST':
#         findId = re.findall('[^A-Za-z0-9!@#]',request.form['uid'])
#         findPw = re.findall('[^A-Za-z0-9!@#]', request.form['pw'])
#         if bool(findId) == True or len(request.form['uid']) < 6:
#             return 'Invaild format'
#         if bool(findPw) == True or len(request.form['pw']) < 8:
#             return 'Invaild format'
#         if request.form['uid'] in data:
#             return 'this ID is exist, push other ID'
#         else:
#             data[request.form['uid']]=request.form['pw']
#     return render_template('create.html')
#
#
# if __name__=='__main__':
#     app.run()
from flask import Flask, session

app = Flask(__name__)

#app.secret_key = 'You Will Never Guess'


@app.route('/setuser/<user>')
def setuser(user):
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser():
    return 'User value was previously set to: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)