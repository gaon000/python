# import pymongo
#
# connection = pymongo.MongoClient("localhost")
# db=connection.signup
# collection = db.data
# data=collection.find()
# print(data[0]['1'])
# from flask import request
# from flask import jsonify
# from flask import Flask, session
#
# app = Flask(__name__)
# @app.route("/get_my_ip", methods=["GET"])
# def get_my_ip():
#     print(request.remote_addr)
#     return jsonify({'ip': request.remote_addr}), 200
# @app.route('/login')
# def login():
#     session[request.remote_addr]=True
# @app.route('/')
# def ma():
#     if session[request.remote_addr]!=True:
#         return 'get out'
#     else:
#         return 'welcome'
# app.secret_key='kak'
# app.run(debug=True)
from flask import Flask, session, redirect, url_for, escape, request,jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    # if request.remote_addr in session:
    #     # return 'Logged in as %s' % escape(session['username'])
    #     return 'logged in'
    return request.remote_addr

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session[request.remote_addr] = 'confirm'
        return redirect(url_for('index'))
    return render_template('login.html')
    #     <form action="" method="post">
    #         <p><input type=text name=username>
    #         <p><input type=submit value=Login>
    #     </form>
    # '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop(request.remote_addr,None)
    return redirect(url_for('index'))
app.secret_key='asdf'
app.run()