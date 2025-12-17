"""
Understand MS graph permissions
https://learn.microsoft.com/en-us/graph/permissions-reference


In this code , I used the Azure AD CLI app id
https://learn.microsoft.com/en-us/power-platform/admin/apps-to-allow

I tried various scopes

"""

# How to get the Azure CLI app id  - this is the well published app
# https://github.com/Azure/azure-cli/issues/28628
# Given the client ID and tenant ID for an app registered in Azure,
# provide a <ms-entra-id> access token and a refresh token.

# If the caller is not already signed in to Azure, the caller's
# web browser will prompt the caller to sign in first.


import os
from msal import PublicClientApplication
import dotenv


dotenv.load_dotenv(override=True)
# did not work , Consent error
azure_client_id = "04b07795-8ddb-461a-bbee-02f9e1bf7b46"
tenant_id = os.environ["AZURE_TENANT_ID"]
print(f"client_id: {azure_client_id}, tenant_id: {tenant_id}")

# Do not modify this variable. It represents the programmatic ID for
# Enter the scope of DB registar scope url.
# scopes = ["Sites.ReadWrite.All"] #did not work
# Authentication failed. invalid_request: AADSTS65002: Consent between first party application '04b07795-8ddb-461a-bbee-02f9e1bf7b46' and first party resource '00000003-0000-0000-c000-000000000000' must be configured via preauthorization - applications owned and operated by Microsoft must get approval from the API owner before requesting tokens for that API. Trace ID: b9f3b4ff-9978-445d-935e-bf1a53840700 Correlation ID: 883c94b3-e304-4b24-9827-da49df15db9e Timestamp: 2025-12-16 22:44:29Z. (https://login.microsoftonline.com/error?code=65002)
# This works with Azure CLI az account get-access-token --resource-type ms-graph

# scopes = ["https://graph.microsoft.com/"] #did not work
# he scope format is invalid. Scope must be in a valid URI form <https://example/scope> or a valid Guid <guid/scope>.

graph_scope = "https://graph.microsoft.com/.default"  # this worked
sp_guid_scope = "00000003-0000-0ff1-ce00-000000000000"
scopes = [sp_guid_scope]
# this worked too az account get-access-token --scope "https://graph.microsoft.com/.default"
app = PublicClientApplication(
    client_id=azure_client_id,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)


# try this scope https://stackoverflow.com/a/63386756/2989655

acquire_tokens_result = app.acquire_token_interactive(
    scopes=scopes
)

if 'error' in acquire_tokens_result:
    print("Error: " + acquire_tokens_result['error'])
    print("Description: " + acquire_tokens_result['error_description'])
else:
    print("Access token:\n")
    print(acquire_tokens_result['access_token'])
    print("\nRefresh token:\n")
    # print(acquire_tokens_result['refresh_token'])
