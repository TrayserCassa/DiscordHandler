import requests
import json

headers = {

    'User-Agent': "FeuerwehrApp",
    
    "Content-Type": "application/json"

}

url = "https://discordapp.com/api/webhooks/320293246213554178/oMqpuCQDZvI8ww2CaJbc4d42c18YpJkEp-GdWbBPA6X25lgPugyCFzY_DXEhza5RKGSI"

def send_message(message):
    content = json.dumps({"content": message})
    requ = requests.post(url,
                         headers=headers,
                         data=content)
    print(requ.ok)


send_message("Some lofs")
    
#client.run('MzIwMTgwMjM0MzAzNDM4ODUw.DBMetw.fRdWJfTh2M1WhR3-1a4uOYljtcg')
