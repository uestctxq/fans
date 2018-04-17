from project import app
from flask import render_template, request
@app.route('/')
def start():
    return render_template('index.html')

@app.route('/print',methods=['GET','POST'])
def printer():
    if request.method=='POST':
         return render_template('index.html')
    return render_template('print.html')


