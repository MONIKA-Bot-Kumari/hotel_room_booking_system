from flask import Blueprint, jsonify

from models import db


db_bp = Blueprint("db", __name__)


@db_bp.route("/test-db", methods=["GET"])
def test_db():
    try:
        db.session.execute(db.text("SELECT 1"))

        return jsonify({
            "status": "success",
            "message": "Database Connected"
        }), 200

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "status": "error",
            "message": "Database Connection Failed",
            "detail": str(e)
        }), 500