from flask import Flask,render_template,request
from empdata import employee
app=Flask(__name__)
getemployee = Employee()


@app.route('/')
def index():
    return render_template('home.html')
@app.route('/employee')
def employee():
    return render_template('empdata.html',myemployee=getemployee)  

if(__name__=='__main__'):
    app.run(debug=True)      

