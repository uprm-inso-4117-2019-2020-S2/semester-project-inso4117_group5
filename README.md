# Help the Homies get Relief

## Installation
### Setting up the virtual environment
Install virtualenv package:
```bash
$ pip install virtualenv
```

Create virtual environment, on project folder run:
```bash
$ virtualenv venv
```

Activate virtual environment by running the following command:

* Windows:
```bash
> source \venv\Scripts\activate.bat
```
* Linux/MAC OS:
```bash
$ source venv/bin/activate
```

Install project dependencies in the virtual environment:
```bash
(venv) ..$ pip install -r requirements.txt
```

## Run the application
This section contains instruction son how to run the Flask application in development and debug mode enabled.
Make sure to have your **venv** activated.

We must first specify three environment variables to tell Flask to run the application on these configurations.
On the project folder, create a new file called `.flaskenv` In the file add the following lines.

```
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
```

To run the application simply run:
```bash
(venv) ..$ flask run

(you should get something like this)
* Serving Flask app "app.py" (lazy loading)
* Environment: development
* Debug mode: on
...
```
