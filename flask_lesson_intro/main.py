from flask import Flask, render_template
from flask_lesson_intro.utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/<gadget>/info')
def get_info(gadget):
    info = [dict_ for dict_ in get_data() if gadget.replace('_', ' ').lower() in
            (val.lower() for val in dict_.values())][0]
    return render_template("info.html", info=info, gadget=gadget)

@app.route('/author')
def author_page():
    return render_template("author.html")

if __name__ == "__main__":
    app.run(debug=True)
