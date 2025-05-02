[[_TOC_]]

# About
Demonstrates Azure AD integration with Python Flask

---

# Summary steps from copilot
[Steps from Copilot](docs/copilot.md)

----

# How does login_manger work ?

## Step-0-Configure login_manager
You need to specify the route which will do the login operation

## Step-1-Handle getAToken end point

This method receives the JWT token. Decode the `email` and `name` attributes from the token and invoke the method `login_user` 

## Step-1-user_loader method to intercept all calls

This will create an `User` object by reading `email` and `name` from `session`

## Step-3-Protect the views using `@login_required`

- This will kick off the login sequence whenever somebody tries to hit the protected route. 
- The login route specified while configuring `login_manager` will be invoked

---

# App registration

## Redirect URL
![alt text](docs/images/azure_app_registration.png)

## Client Secret

![alt text](docs/images/client_secret.png)

## Client ID and Tenant ID

![alt text](docs/images/client_id.png)

---

# Configuring Flask session

## File system 
https://stackoverflow.com/questions/53841909/clean-server-side-session-files-flask-session-using-filesystem

```python
# __init__.py

from flask_session import Session
from datetime import timedelta

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)

# The maximum number of items the session stores 
# before it starts deleting some, default 500
app.config['SESSION_FILE_THRESHOLD'] = 100  
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SESSION_FILE_DIR'] = '/path/to/session/folder'  # Specify your folder path here
sess = Session()
sess.init_app(app)
```

