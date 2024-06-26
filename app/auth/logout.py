from . import auth_bp


@auth_bp.route("/logout")
def user_logout():
    
    return "<h2>User Logout</h2>"