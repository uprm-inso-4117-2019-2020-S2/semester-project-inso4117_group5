from flask import Flask, jsonify, request , redirect , url_for, render_template
from flask_cors import CORS, cross_origin
from passlib.hash import sha256_crypt
from domainHandler.user import UserHandler
from domainHandler.ticket import TicketHandler
# Apply CORS to this app
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # This makes jsonify NOT sort automatically.
CORS(app)


@app.route('/')
def home():
    return render_template("selection.html")

@app.route('/provider')
def provider():
    return render_template("provider.html")

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
        username = request.json['username']
        password = request.json['password']
        password_hash = sha256_crypt.encrypt(password)
        # these are to be used in do_register
        # email = request.json['email']
        # phone = request.json['phone']

        UserHandler().do_register(request.json)
        if UserHandler().do_login(username, password):
            flash(f'Account created for {username}!', 'success')
            return redirect(url_for('/')) #this route will change
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
