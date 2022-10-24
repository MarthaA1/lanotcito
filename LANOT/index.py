# It imports the Flask class from the flask module.
from flask import Flask, render_template

# It creates a Flask application object.
app = Flask(__name__)


# It renders the template called inicio.html and returns it to the user. :return: the template 'inicio.html'
@app.route('/')
def home():
    return render_template('inicio.html')

# It takes the URL '/about' and renders the template 'info.html' :return: the template 'info.html'
@app.route('/about')
def about():
    return render_template('info.html')


# Running the app on the localhost.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
