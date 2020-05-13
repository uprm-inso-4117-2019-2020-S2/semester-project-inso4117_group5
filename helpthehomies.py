from flask import Flask, jsonify, request , redirect , url_for, render_template, session
from flask_cors import CORS, cross_origin
from domainHandlers.user import UserHandler
from domainHandlers.user import RequestHandler

# Apply CORS to this app
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # This makes jsonify NOT sort automatically.
CORS(app)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/HTH/login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        if UserHandler().do_login(username, password):
            return jsonify(logged_in=True, username=username)
        else:

            return jsonify(logged_in=False)


@app.route('/helpsomehommies', methods=['POST', 'GET'])
def Request_feed():
    if request.method == 'GET':
        allreqs = RequestHandler().get_all_requests()
        return render_template("provider.html", Requests = allreqs)


@app.route('/requester')
def requester():
    return render_template("requester.html")


@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserHandler().get_all_users()
    if request.method == 'POST':
        return UserHandler().insert_user(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/user/<int:uid>', methods=['GET'])
def user(uid: int):
    if request.method == 'GET':
        return UserHandler().get_user_by_id(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

#TODO these need the DAO to work
# @app.route('/ticket', methods=['GET', 'POST'])
# def tickets():
#     if request.method == 'GET':
#         return TicketHandler().get_all_tickets()
#     if request.method == 'POST':
#         return TicketHandler().insert_ticket(request.json)
#     else:
#         return jsonify(Error="Method not allowed."), 405
#
#
# @app.route('/ticket/<int:uid>', methods=['GET'])
# def get_ticket(uid: int):
#     if request.method == 'GET':
#         return TicketHandler().get_ticket_by_id(uid)
#     else:
#         return jsonify(Error="Method not allowed."), 405


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
            return redirect(url_for('/helpsomehommies'))
        return render_template('register.html')


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
