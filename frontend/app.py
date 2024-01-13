from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)


@app.route("/")
def home_page():
    current_year = datetime.datetime.now().year
    return render_template('index.html', current_year=current_year)


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


if __name__ == "__main__":
    app.run(debug=True)
