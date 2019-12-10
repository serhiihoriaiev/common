from flask import Flask

from config import get_config
from create_db import create_db_bp
from db import db
from rooms import rooms_bp
from staff import staff_bp
from tenants import tenants_bp

app = Flask(__name__)
app.config.from_object(get_config())
db.init_app(app)

app.register_blueprint(create_db_bp)
app.register_blueprint(rooms_bp)
app.register_blueprint(tenants_bp)
app.register_blueprint(staff_bp)

if __name__ == '__main__':
    app.run(debug=True)
