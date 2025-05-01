from flask import Flask, redirect, url_for, session
from flask import render_template, request
from msal import ConfidentialClientApplication
import os
import dotenv

dotenv.load_dotenv(override=True)
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a secure key in production

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
    return f"Hello, {session['user']['name']}!"


@app.route("/login")
def login():
    auth_url = msal_app.get_authorization_request_url(
        SCOPE, redirect_uri=url_for("authorized", _external=True)
    )
    return redirect(auth_url)


@app.route(REDIRECT_PATH)
def authorized():
    code = request.args.get("code")
    if not code:
        return "Authorization failed.", 400

    result = msal_app.acquire_token_by_authorization_code(
        code, scopes=SCOPE, redirect_uri=url_for("authorized", _external=True)
    )

    if "id_token_claims" in result:
        session["user"] = {
            "name": result["id_token_claims"]["name"],
            "email": result["id_token_claims"]["preferred_username"],
        }
        return redirect(url_for("index"))
    else:
        return f"Login failed: {result.get('error_description')}", 400


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        f"{AUTHORITY}/oauth2/v2.0/logout?post_logout_redirect_uri={url_for('index', _external=True)}"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
