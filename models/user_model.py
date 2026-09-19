from models import fetch_records, insert_record


def get_user_by_email(email):
    query = """
        SELECT *
        FROM users
        WHERE email = :email
    """

    records = fetch_records(
        query,
        {"email": email}
    )

    return records[0] if records else None


def create_user(name, email, password, phone_number):
    query = """
        INSERT INTO users
        (name, email, password, role, phone_number)
        VALUES
        (:name, :email, :password, :role, :phone_number)
    """

    params = {
        "name": name,
        "email": email,
        "password": password,
        "role": "Guest",
        "phone_number": phone_number
    }

    return insert_record(query, params)