from flask import render_template
from view import bp

@bp.route("/")
def main():
    return render_template("main.html")

