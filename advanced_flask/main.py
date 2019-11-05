from flask import Flask, render_template, session

from products.prod_main import prod
from supermarkets.super_main import sup

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(prod)
app.register_blueprint(sup)


@app.route('/')
@app.route('/home')
def get_home():
    return render_template("home.html")


@app.errorhandler(404)
def get_404(error):
    return render_template('404.html')


@app.route('/restart')
def restart_session():
    session.clear()
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
