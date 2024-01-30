from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
import os
import requests
from Helpers.userMethods import check_user_credentials, check_user_name, get_user_by_id
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

# ///////////////////// Configuration block ///////////////////// #

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
app.config['SECRET_KEY'] = f'{os.environ.get("secret")}'
host_ip = f'{os.environ.get("host_ip")}'
backendapi_port = f'{os.environ.get("backend_port", 3001)}'
BACKEND_API_BASE_URL = f"http://{host_ip}:{backendapi_port}"

# ///////////////////// Authentication block ///////////////////// #


class User(UserMixin):
    def __init__(self, user_json):
        self.user_json = user_json

    def get_id(self):
        object_id = self.user_json.get('userId')
        return int(object_id)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    user_info = get_user_by_id(user_id)
    return User(user_info)

# ///////////////////// Application routes ///////////////////// #


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('login.html')


@app.route("/record", methods=['GET', 'POST'])
@login_required
def record():
    if request.method == 'GET':
        transaction_list = requests.get(
            f"{BACKEND_API_BASE_URL}/api/v2/Transaction/transactionlists", verify=False).json()
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
            user_object = check_user_name(username)
            user = User(user_object)
            login_user(user)
            return redirect(url_for('record'))

        return redirect(url_for('login'))


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    request_body = {
        "userName": f"{request.form['userName']}",
        "password": f"{request.form['password']}"
    }
    response_data = requests.post(
        f"{BACKEND_API_BASE_URL}/api/v2/auth/user/register", verify=False, json=request_body)
    if response_data.status_code == 200:
        return redirect(url_for('record'))
    else:
        flash("Error creating account. Please check your input or try again!", "error")
    return redirect(url_for('register'))


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    if request.method == 'GET':
        response_data = requests.get(
            f"{BACKEND_API_BASE_URL}/api/v2/Transaction/{id}", verify=False)
        if response_data.status_code == 200:
            json_content = response_data.json()
            return render_template('edit.html', record=json_content["data"])
        else:
            flash(
                f"Error editing record with id {id}. Please try again!", "error")
            return redirect(url_for("record"))
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


@app.route("/summary", methods=['GET', 'POST'])
@login_required
def summary():
    if request.method == 'GET':
        return render_template('stats.html')
    else:
        request_body = {
            "startTime": f"{request.form['startDate']}",
            "endtime": f"{request.form['endDate']}"
        }
        respose_data = requests.post(
            f"{BACKEND_API_BASE_URL}/api/v2/Transaction/summary", verify=False, json=request_body)
        if respose_data.status_code == 200:
            json_content = respose_data.json()
            record_summary = json_content['data']
            return render_template('stats.html',
                                   record_summary=record_summary,
                                   start_date=request.form['startDate'],
                                   end_date=request.form['endDate']
                                   )
        else:
            flash("Error retiving transaction summary. Please try again!", "error")
            return redirect(url_for('summary'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('notfound.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
