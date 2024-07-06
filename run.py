from flask import render_template, request, url_for
from app import create_app


app = create_app()

@app.route("/")
def index():
    "The Index Page"
    
    return render_template(
        "index.html",
        login_url=url_for("auth.user_checkpoint"))


@app.route("/test")
def test_route():
    return render_template("layout.html")


if __name__ == "__main__":
    app.run()