from flask import Flask, jsonify, request , redirect , url_for, render_template, session, flash
from flask_cors import CORS, cross_origin
from domainHandlers.user import UserHandler
from domainHandlers.request import RequestHandler

import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Apply CORS to this app
template_dir = "./templates"
static_dir = "./static"
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = '5791628bb0b13ce0c676dfde280ba245'
app.config['JSON_SORT_KEYS'] = False  # This makes jsonify NOT sort automatically.
CORS(app)


@app.route('/')
def home():
    session['logged_in'] = False
    return render_template("home.html")


@app.route('/HTH/profile', methods=['GET','POST'])
def profile():
    if session['logged_in']:
        if request.method == 'GET':
            user_info = UserHandler().get_user_by_id(session['uid'])
            unf_req = RequestHandler().get_requests_by_user_status(session['uid'],'fuf')
            inprog_req = RequestHandler().get_requests_by_user_status(session['uid'],'unfuf')
            fufld_req = RequestHandler().get_requests_by_user_status(session['uid'],'pending')
            return render_template("userProfile.html", Info = user_info, Unf = unf_req , Inp = inprog_req , Fuf = fufld_req)

    else:
        return redirect(url_for('user_login'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    if request.method == 'POST':
        username = request.json['uusername']
        password = request.json['upassword']
        UserHandler().do_register(request.json)
        if UserHandler().do_login(username, password):
            return jsonify(signedIn=True)




@app.route('/HTH/login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        username = request.json['uusername']
        password = request.json['upassword']

        if UserHandler().do_login(username, password):
            return jsonify(logged_in=True)

        else:
            return jsonify(logged_in=False)


@app.route('/HTH/logout', methods=['GET'])
def user_logout():
    if request.method == 'GET':
        if UserHandler().do_logout():
            return redirect(url_for('home'))


@app.route('/helpsomehommies', methods=['POST', 'GET'])
def Request_feed():
    if session['logged_in']:
        if request.method == 'GET':
            allreqs = RequestHandler().get_all_requests()
            return render_template("provider.html", Requests = allreqs)
        if request.method == 'POST':
            return RequestHandler().insert_request(request.json)
    else:
        return redirect(url_for('user_login'))



@app.route('/requests', methods=['GET'])
def getreqs():
    if request.method == 'GET':
        allreqs = RequestHandler().get_all_requests()
        return(allreqs)


@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserHandler().get_all_users()
    if request.method == 'POST':
        return UserHandler().insert_user(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/user/<int:uid>', methods=['GET', 'DELETE'])
def user(uid: int):
    if request.method == 'GET':
        return UserHandler().get_user_by_id(uid)
    elif request.method == 'DELETE':
        return UserHandler().delete_user_by_id(uid)
    else:
        return jsonify(Error="Method not allowed."), 405


if __name__ == '__main__':
    app.run(debug=True)
