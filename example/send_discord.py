import json
import requests

def main():

    webhook_url = 'https://discordapp.com/api/webhooks/322137744224681984/RiMBt_rczJBenutdYetPeADhGLsahstswZ0KVZZN7pIxN1clLrpSqcbo5GcR49StO22p'
    agent = 'Testing'

    message = 'I’m not lazy, I’m energy efficient'
    
    content = json.dumps({"content": message})

    header =  {
        'User-Agent': agent,
        "Content-Type": "application/json"
    }
    
    request = requests.post(webhook_url,
                            headers=header,
                            data=content)

if __name__ == '__main__':
    main()
