import logging
import os
from datetime import datetime
from flask import Flask, redirect, url_for, session
from flask import request
from msal import ConfidentialClientApplication
from flask_login import login_required, LoginManager, UserMixin, login_user
import dotenv
import dash


dotenv.load_dotenv(override=True)
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a secure key in production

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirect to login page if not authenticated

# Configure Dash app
# context


class User(UserMixin):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

#
# Exception: Missing user_loader or request_loader. Refer to http://flask-login.readthedocs.io/#how-it-works for more info.
#


@login_manager.user_loader
def load_user(user_id):
    logging.info(f"load_user ID: {user_id}")
    user = session.get("user")
    if user and user["id"] == user_id:
        return User(user["id"], user["name"], user["email"])
    return None


# Azure AD Configuration
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
AUTHORITY = os.environ["AUTHORITY"]
REDIRECT_PATH = "/getAToken"
SCOPE = ["User.Read"]  # Add other scopes as needed

# MSAL Confidential Client
msal_app = ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET,
)


@app.route("/")
def index():
    if not session.get("user"):
        return redirect(url_for("login"))
    return f"Hello, {session['user']['name']}! , current time is {datetime.now()}"


@app.route("/secureview")
@login_required
def secure_view():
    """
    This method is decorated with @login_required and forces the user to be authenticated before accessing this view.
    """
    return f"Hello, this is a secure view {session['user']['name']}!"


@app.route("/unsecureview")
def un_secure_view():
    """
    This is an un-secure view. It does not require authentication.
    """
    return f"Hello, this is a un-secure view {datetime.now()}"


@app.route("/login")
def login():
    auth_url = msal_app.get_authorization_request_url(
        SCOPE, redirect_uri=url_for("authorized", _external=True)
    )
    return redirect(auth_url)


@app.route(REDIRECT_PATH)
def authorized():
    logging.info(
        f"Redirected to {REDIRECT_PATH} count of args={len(request.args)}")

    code = request.args.get("code")
    if not code:
        return "Authorization failed.", 400

    result = msal_app.acquire_token_by_authorization_code(
        code, scopes=SCOPE, redirect_uri=url_for("authorized", _external=True)
    )

    if "id_token_claims" in result:
        new_user = {
            "id": result["id_token_claims"]["preferred_username"].lower(),
            "name": result["id_token_claims"]["name"],
            "email": result["id_token_claims"]["preferred_username"],
        }
        session["user"] = new_user
        login_user(User(new_user["id"], new_user["name"], new_user["email"]))
        # Note - we are forced to finally redirect to the index page.
        # This is because the at this point we have lost the information about the original page the user was trying to access.
        return redirect(url_for("index"))
    else:
        return f"Login failed: {result.get('error_description')}", 400


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        f"{AUTHORITY}/oauth2/v2.0/logout?post_logout_redirect_uri={url_for('index', _external=True)}"
    )


with app.app_context():
    logging.info("Inside app_context")
    dash_app = dash.Dash(use_pages=True, server=app,
                         prevent_initial_callbacks=True,
                         url_base_pathname="/dash/")


@app.before_request
def before_app_request():
    current_path = request.path
    current_url = request.url
    logging.info(f"Before request: Path = {current_path}, URL = {current_url}")
    if not current_path.startswith("/dash/"):
        return
    if not session.get("user"):
        logging.info("User not authenticated, redirecting to login")
        return redirect(url_for("login"))
    else:
        logging.info(f"User authenticated: {session['user']['name']}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
