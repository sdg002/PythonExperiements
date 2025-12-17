# How to get the Azure CLI token id
# https://github.com/Azure/azure-cli/issues/28628
# Given the client ID and tenant ID for an app registered in Azure,
# provide a <ms-entra-id> access token and a refresh token.

# If the caller is not already signed in to Azure, the caller's
# web browser will prompt the caller to sign in first.

# pip install msal
import os
from msal import PublicClientApplication
import sys
import dotenv

# You can hard-code the registered app's client ID and tenant ID here,
# or you can provide them as command-line arguments to this script.

dotenv.load_dotenv(override=True)
client_id = os.environ["AZURE_CLI_CLIENT_ID"]
tenant_id = os.environ["AZURE_TENANT_ID"]
print(f"client_id: {client_id}, tenant_id: {tenant_id}")

# Do not modify this variable. It represents the programmatic ID for
# Enter the scope of DB registar scope url.
# scopes = ["Sites.ReadWrite.All"] #did not work
# Authentication failed. invalid_request: AADSTS65002: Consent between first party application '04b07795-8ddb-461a-bbee-02f9e1bf7b46' and first party resource '00000003-0000-0000-c000-000000000000' must be configured via preauthorization - applications owned and operated by Microsoft must get approval from the API owner before requesting tokens for that API. Trace ID: b9f3b4ff-9978-445d-935e-bf1a53840700 Correlation ID: 883c94b3-e304-4b24-9827-da49df15db9e Timestamp: 2025-12-16 22:44:29Z. (https://login.microsoftonline.com/error?code=65002)
# This works with Azure CLI az account get-access-token --resource-type ms-graph

# scopes = ["https://graph.microsoft.com/"] #did not work
# he scope format is invalid. Scope must be in a valid URI form <https://example/scope> or a valid Guid <guid/scope>.

scopes = ["https://graph.microsoft.com/.default"]  # this worked
app = PublicClientApplication(
    client_id=client_id,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

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
