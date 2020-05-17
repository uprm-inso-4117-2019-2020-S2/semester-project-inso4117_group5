from flask import Flask, jsonify, request , redirect , url_for, render_template, session, flash
from flask_cors import CORS, cross_origin
from domainHandlers.user import UserHandler
from domainHandlers.request import RequestHandler

from config import app


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/HTH/profile', methods=['GET'])
def profile():
    try:
        if session['logged_in']:
            if request.method == 'GET':
                user_info = UserHandler().get_user_by_id(session['uid'])
                unf_req = RequestHandler().get_requests_by_user_status(session['uid'],0)
                inprog_req = RequestHandler().get_requests_by_user_status(session['uid'],1)
                fufld_req = RequestHandler().get_requests_by_user_status(session['uid'],2)

                return render_template("userProfile.html", Info = user_info, Unf = unf_req , Inp = inprog_req , Fuf = fufld_req)
        else:
            return redirect(url_for('user_login'))
    except:
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
            flash(f'Account created for {username}!', 'success')
            return redirect(url_for('profile'))
        return render_template('register.html')


@app.route('/HTH/login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        username = request.json['uusername']
        password = request.json['upassword']
        if UserHandler().do_login(username, password):
            return redirect(url_for('Request_feed'))
        else:

            return jsonify(logged_in=False)


@app.route('/HTH/logout', methods=['GET'])
def user_logout():
    if request.method == 'GET':
        if UserHandler().do_logout():
            return redirect(url_for('home'))


@app.route('/helpsomehommies', methods=['POST', 'GET'])
def Request_feed():
    try:
        if session['logged_in']:
            if request.method == 'GET':
                allreqs = RequestHandler().get_all_requests()
                return render_template("provider.html", Requests = allreqs)
            if request.method == 'POST':
                req = RequestHandler().insert(request.json)
        else:
            return redirect(url_for('user_login'))
    except:
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
