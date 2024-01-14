from flask import Flask, render_template, request, redirect
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home_page():
    transaction_list = requests.get(
        "http://localhost:3001/api/v2/Transaction/transactionlists").json()
    current_year = datetime.datetime.now().year
    return render_template('index.html', current_year=current_year, transactionList=transaction_list)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print(
            f"Username: {request.form['userName']} and password: {request.form['password']}")
        return redirect('/login')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/edit/<int:id>")
def edit(id, methods=['GET', 'POST']):
    if request.method == 'GET':
        return "Ok"


if __name__ == "__main__":
    app.run(debug=True)
