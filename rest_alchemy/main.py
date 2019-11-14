from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy

from config import get_config

app = Flask(__name__)
app.config.from_object(get_config())
db = SQLAlchemy(app)


@app.route('/health')
def health_check():
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)
