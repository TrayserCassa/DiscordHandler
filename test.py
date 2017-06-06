import requests
import json
import Handler

headers = {

    'User-Agent': "FeuerwehrApp",

    "Content-Type": "application/json"

}

url = ""


def send_message(message):
    content = json.dumps({"content": message})
    requ = requests.post(url,
                         headers=headers,
                         data=content)
    print(requ.ok)


send_message("Some lofs")
