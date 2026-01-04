"""


In this code , I am trying wiht SharePoint client id
https://learn.microsoft.com/en-us/power-platform/admin/apps-to-allow

# try this scope https://stackoverflow.com/a/63386756/2989655

"""


import os
from msal import PublicClientApplication
import dotenv


dotenv.load_dotenv(override=True)
SHAREPOINT_CLIENT_ID = "d326c1ce-6cc6-4de2-bebc-4591e5e13ef0"
tenant_id = os.environ["AZURE_TENANT_ID"]
print(f"client_id: {SHAREPOINT_CLIENT_ID}, tenant_id: {tenant_id}")


SP_GUID_SCOPE = "00000003-0000-0ff1-ce00-000000000000"
scopes = [SP_GUID_SCOPE]
app = PublicClientApplication(
    client_id=SHAREPOINT_CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

print(f"Going to acquire token with client id={SHAREPOINT_CLIENT_ID}")
acquire_tokens_result = app.acquire_token_interactive(
    scopes=scopes
)
print(acquire_tokens_result)
if 'error' in acquire_tokens_result:
    print("Error: " + acquire_tokens_result['error'])
    print("Description: " + acquire_tokens_result['error_description'])
else:
    print("Access token:\n")
    print(acquire_tokens_result['access_token'])
    print("\nRefresh token:\n")
    # print(acquire_tokens_result['refresh_token'])
