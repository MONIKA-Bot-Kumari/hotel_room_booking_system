from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.user_models import get_user_by_email, create_user


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        phone_number = request.form.get("phone_number", "").strip()

        # Check empty fields
        if not name or not email or not password or not phone_number:
            flash("All fields are required.", "error")
            return render_template("register.html")

        # Check email format
        if "@" not in email:
            flash("Please enter a valid email address.", "error")
            return render_template("register.html")

        # Check duplicate email
        existing_user = get_user_by_email(email)

        if existing_user:
            flash("Email already registered.", "error")
            return render_template("register.html")

        # Create user
        create_user(
            name,
            email,
            password,
            phone_number
        )

        flash(
            "Registration successful. Please login to continue.",
            "success"
        )

        return render_template("register.html")

    return render_template("register.html")