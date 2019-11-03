from flask import Flask, render_template

from advanced_flask.products.prod_main import prod

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(prod)

@app.route('/')
@app.route('/home')
def get_home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
