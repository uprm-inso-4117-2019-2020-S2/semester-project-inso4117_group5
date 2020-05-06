from flask import Flask, jsonify, request , redirect , url_for, render_template
from flask_cors import CORS, cross_origin
from domainHandlers.user import UserHandler
# Apply CORS to this app
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
CORS(app)
#lol
user = [1,'Morsa','faces44','morsa@gmail.com','7899','Quebra',.99]

@app.route('/usertest')
def userTest():
    userdict= {}
    if UserHandler().validateUser(user):
        userdict = UserHandler().createUserDict(user)
    return jsonify(User=userdict)



@app.route('/')
def home():
    return render_template("selection.html")

@app.route('/provider')
def provider():
    return render_template("provider.html")

@app.route('/requester')
def requester():
    return render_template("requester.html")

#
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('/'))
#     return render_template('register.html', title='Register', form=form)
#
#
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
