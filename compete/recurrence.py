from  flask import Flask,render_template,request,flash
from Recur import *


app = Flask(__name__)

app.secret_key = "dont tell anyone"


@app.route('/show' , methods=['POST'])
def show():
    name = request.form['names']
    print(name)
    arr = validation(name)
    #s = "n^" +str(arr[0])+"(log n)^"+str(arr[1])

    if arr[0] == 'V' or arr[0] == 'i':
        flash(arr)
        return render_template('index.html',g="no")
    elif arr[1] == 0 :
        return render_template( 'index.html', s = str(arr[0]) , g="yes")
    else :
        return render_template('index.html', s=str(arr[0]), g=str(arr[1]))



@app.route('/')
def home() :
    return render_template('show.html')




app.run(debug=True)

