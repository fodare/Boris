from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
import os
import requests
from Helpers.userMethods import check_user_credentials, check_user_name

app = Flask(__name__)
app.secret_key = f'{os.environ.get("secret")}'
BACKEND_API_BASE_URL = 'http://localhost:3001'


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('login.html')


@app.route("/record", methods=['GET', 'POST'])
def record():
    if request.method == 'GET':
        transaction_list = requests.get(
            f"{BACKEND_API_BASE_URL}/api/v2/Transaction/transactionlists").json()
        current_year = datetime.datetime.now().year
        return render_template('index.html', current_year=current_year,
                               transactionList=transaction_list)
    else:
        request_body = {
            "amount": f"{request.form['amount']}",
            "type": f"{request.form['type']}",
            "tag": f"{request.form['tag']}",
            "note": f"{request.form['note']}"
        }
        response_data = requests.post(
            f"{BACKEND_API_BASE_URL}/api/v2/Transaction/addtransaction", json=request_body)
        if response_data.status_code == 200:
            return redirect(url_for('record'))
        else:
            flash(
                "Error recording transaction. Please check you input and try again!", 'error')
            return redirect(url_for('record'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['userName']
        password = request.form['password']
        if check_user_credentials(username, password):
            return redirect(url_for('record'))

        return redirect(url_for('login'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    request_body = {
        "userName": f"{request.form['userName']}",
        "password": f"{request.form['password']}"
    }
    response_data = requests.post(
        f"{BACKEND_API_BASE_URL}/api/v2/auth/user/register", json=request_body)
    if response_data.status_code == 200:
        return redirect(url_for('record'))
    else:
        flash("Error creating account. Please check your input or try again!", "error")
    return redirect(url_for('register'))


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        response_data = requests.get(
            f"{BACKEND_API_BASE_URL}/api/v2/Transaction/{id}")
        if response_data.status_code == 200:
            json_content = response_data.json()
            return render_template('edit.html', record=json_content["data"])
        else:
            flash(
                f"Error editing record with id {id}. Please try again!", "error")
            return redirect('home_page')
    else:
        request_body = {
            "amount": f"{request.form['amount']}",
            "transactionType": f"{request.form['type']}",
            "transactionTag": f"{request.form['tag']}",
            "note": f"{request.form['note']}"
        }
        response_data = requests.put(
            f"{BACKEND_API_BASE_URL}/api/v2/Transaction/updatetransaction/{id}", json=request_body)
        if response_data.status_code == 200:
            return redirect(url_for('record'))
        else:
            flash(
                f"Error editing record with id {id}. Please check your input and try again", "error")
            return redirect(url_for('edit', id=id))


@app.route("/summary")
def summary():
    return render_template('stats.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('notfound.html')


if __name__ == "__main__":
    app.run(debug=True)
