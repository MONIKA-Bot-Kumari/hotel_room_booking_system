import os
from urllib.parse import quote_plus

from flask import Flask
from dotenv import load_dotenv

from models import db
from controllers.db_controller import db_bp
from controllers.main_controller import main_bp
from controllers.auth_controller import auth_bp

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = "hotel-booking-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://"
    f"{quote_plus(os.getenv('DB_USER'))}:"
    f"{quote_plus(os.getenv('DB_PASSWORD'))}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(db_bp)
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True, port=5001)