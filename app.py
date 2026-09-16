import os
from urllib.parse import quote_plus

from flask import Flask
from dotenv import load_dotenv

from models import db
from controllers.main_controller import main_bp
from controllers.db_controller import db_bp
from controllers.auth_controller import auth_bp


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "hotel-booking-secret-key"
)

db_user = os.getenv("MYSQL_USER")
db_password = os.getenv("MYSQL_PASSWORD")
db_host = os.getenv("MYSQL_HOST", "localhost")
db_port = os.getenv("MYSQL_PORT", "3306")
db_name = os.getenv("MYSQL_DATABASE", "hotel_booking")

db_password = quote_plus(db_password or "")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{db_user}:{db_password}"
    f"@{db_host}:{db_port}/{db_name}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(main_bp)
app.register_blueprint(db_bp)
app.register_blueprint(auth_bp)

if __name__=="__main__":
    app.run(debug=True, port=5001)