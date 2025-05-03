[[_TOC_]]

# Step 1: **Set Up Your Azure AD Tenant**
1. **Create an Azure AD tenant** if you don't have one already.
2. **Register your Flask application** in the Azure AD portal:
   - Go to **Azure Active Directory** > **App registrations** > **New registration**.
   - Enter a name for your app.
   - Set the **Redirect URI** to your Flask app's URL (e.g., `http://localhost:5000/login/callback`).

# Step 2: **Install Required Packages**
Install the necessary Python packages:

```bash
pip install Flask msal requests
```

# Step 3: **Configure Flask Application**
Set up your Flask app with the necessary configurations:

```python
from flask import Flask, redirect, url_for, session
from msal import ConfidentialClientApplication

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Azure AD configuration
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
AUTHORITY = 'https://login.microsoftonline.com/your_tenant_id'
REDIRECT_PATH = '/login/callback'
ENDPOINT = 'https://graph.microsoft.com/v1.0/me'
SCOPE = ['User.Read']

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    if 'user' in session:
        return f'Hello, {session["user"]["name"]}!'
    return redirect(url_for('login'))

@app.route('/login')
def login():
    session['flow'] = _build_auth_code_flow()
    return redirect(session['flow']['auth_uri'])

@app.route(REDIRECT_PATH)
def authorized():
    result = _build_msal_app().acquire_token_by_authorization_code(
        request.args['code'],
        scopes=SCOPE,
        redirect_uri=url_for('authorized', _external=True))
    if 'error' in result:
        return f"Error: {result['error']}"
    session['user'] = result.get('id_token_claims')
    return redirect(url_for('index'))

def _build_msal_app():
    return ConfidentialClientApplication(
        CLIENT_ID, authority=AUTHORITY,
        client_credential=CLIENT_SECRET)

def _build_auth_code_flow():
    return _build_msal_app().initiate_auth_code_flow(
        SCOPE, redirect_uri=url_for('authorized', _external=True))

if __name__ == '__main__':
    app.run()
```

# Step 4: **Run Your Flask Application**
Start your Flask application:

```bash
python app.py
```

# Step 5: **Test Authentication**
Navigate to your Flask app in the browser and test the login flow.

Would you like more details on any specific step or have any other questions about Flask or Azure AD?