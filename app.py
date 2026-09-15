from flask import Flask

from controllers.main_controller import main_bp
from controllers.db_controller import db_bp


app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(db_bp)


if __name__ == "__main__":
    app.run(debug=True)