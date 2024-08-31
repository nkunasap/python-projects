from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/androidpublisher']
SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('androidpublisher', 'v3', credentials=credentials)

package_name = 'your.package.name'
edit = service.edits().insert(body={}, packageName=package_name).execute()

apk_path = 'path/to/your/app.apk'
apk_response = service.edits().apks().upload(
    editId=edit['id'],
    packageName=package_name,
    media_body=apk_path).execute()

print('APK uploaded:', apk_response)
