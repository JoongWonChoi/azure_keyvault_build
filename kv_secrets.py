from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential

keyVaultName = "Jwc"
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = AzureCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = input("Input a name for you SECRET > ")
secretValue = input("Input a value for you SECRET > ")

print(f"Creating a secret in {keyVaultName} called '{secretName}' with this value '{secretValue}' . . . ")

client.set_secret(secretName, secretValue)

print("done")

print(f"Retrieving your secret from {keyVaultName}.")
retrieved_secret = client.get_secret(secretName)

print(f"Your secret is '{retrieved_secret.value}'.")

delete = input("Do you wanna delete secrtes? (YES / NO) >> ")

if delete=="YES":
    print(f"Now Deleting your secret from {keyVaultName} . . . ")

    poller = client.begin_delete_secret(secretName)
    deleted_secret = poller.result()

    print("done")







