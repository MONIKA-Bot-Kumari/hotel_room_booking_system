from sqlalchemy import text
from models import db


def execute_query(query, params=None):
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result
    except Exception:
        db.session.rollback()
        raise


def insert_record(query, params=None):
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result.lastrowid
    except Exception:
        db.session.rollback()
        raise


def update_record(query, params=None):
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result.rowcount
    except Exception:
        db.session.rollback()
        raise


def delete_record(query, params=None):
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result.rowcount
    except Exception:
        db.session.rollback()
        raise


def fetch_records(query, params=None):
    try:
        result = db.session.execute(text(query), params or {})
        return result.fetchall()
    except Exception:
        db.session.rollback()
        raise