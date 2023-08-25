import requests

import requests
API = "sec_XPTc23DgFiNZoQEyyR1Dhk1jVOyQBHJ0"
headers = {
    'x-api-key': API,
    "Content-Type": "application/json",
}
text = "que tipos de impeler hay"
string = text.replace('\n',"")
data = {
    'sourceId': ["cha_st6yE6PEKPjkqbE7MnCur","cha_sA7iiViXokux9ikBHAHlG"],
    'messages': [
        {
            'role': "user",
            'content': string,
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)