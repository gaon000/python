# from flask import Flask, render_template, redirect, url_for, request, session
# import pymongo
# from flask import session
# from flask_login import
#
# connection = pymongo.MongoClient("localhost")
# db=connection.signup
# collection = db.data
# data=collection.find()
# app = Flask(__name__)
# @app.route('/')
# def MainPage():
#     return render_template('mainPage.html')
#
# @app.route('/signin', methods=['GET', 'POST'])
# def login():
#     i=0
#     if request.method=="POST":
#         for i in range(data.count()):
#             if data[i].get(request.form['username'])==request.form['password']:
#                 return 'pass'
#             if i==data.count()-1:
#                 return 'retry'
#     return render_template('index.html')
#
# @app.route('/signup',methods=['GET','POST'])
# def signup():
#     i=0
#     if request.method=='POST':
#         for i in range(data.count()):
#             if request.form['uid'] in data[i]:
#                 return 'this ID is exist, push other ID'
#             elif i==data.count()-1:
#                 collection.insert({request.form['uid']:request.form['pw']})
#     return render_template('create.html')
#
#
#
# if __name__=='__main__':
#     app.run()
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/upload', methods = ['GET', 'POST'])
def render_file():
    if request.method == 'POST':
        file = request.files['file[]']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('file_upload.html')

if __name__ == '__main__':
    app.run(debug=True)