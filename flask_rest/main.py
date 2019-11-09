from flask import Flask

from config import run_config
from rooms.rooms_main import rooms_bp
from staff.staff_main import staff_bp
from tenants.ten_main import ten_bp

app = Flask(__name__)
app.config.from_object(run_config)
app.register_blueprint(rooms_bp)
app.register_blueprint(ten_bp)
app.register_blueprint(staff_bp)

if __name__ == '__main__':
    app.run(debug=True)