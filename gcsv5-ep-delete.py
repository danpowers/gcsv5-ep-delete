import globus_sdk

print "SDK version = " + globus_sdk.__version__

client_id=""
client_secret=""
endpoint_uuid=""

cc = globus_sdk.ConfidentialAppAuthClient(client_id,client_secret)
tr = cc.oauth2_client_credentials_tokens()

globus_auth_data = tr.by_resource_server['auth.globus.org']
globus_transfer_data = tr.by_resource_server['transfer.api.globus.org']
globus_auth_token = globus_auth_data['access_token']
globus_transfer_token = globus_transfer_data['access_token']

authorizer = globus_sdk.AccessTokenAuthorizer(globus_transfer_token)
tc = globus_sdk.TransferClient(authorizer=authorizer)

try:
    endpoint = tc.get_endpoint(endpoint_uuid)
except Exception as e:
    print("Error attempting to retrieve endpoint data for uuid: " + str(endpoint_uuid))
    print("\n" + str(e))
    exit(-1)

print("Attempting to delete endpoint with:\n")
print("c_name: " + str(endpoint["canonical_name"]))
print("display name: " + str(endpoint["display_name"]))

try:
    delete_result = tc.delete_endpoint(endpoint_uuid)
except Exception as e:
    print("Error attempting to delete endpoint definition for uuid: " + str(endpoint_uuid))
    print("\n" + str(e))
    exit(-1)

print(str(delete_result))
