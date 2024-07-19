from flask import current_app, render_template, request, url_for
from app import create_app


app = create_app()

@app.route("/")
def index():
    "The Index Page"
    
    return render_template(
        "index.html",
        login_url=url_for("auth.user_checkpoint"))

@app.route("/test_route")
def test_route():
    "Test route"
    
    return render_template(
        "demo/demo_layout.html",)
        #login_url=url_for("auth.user_checkpoint"))
    
    
if __name__ == "__main__":
    app.run()