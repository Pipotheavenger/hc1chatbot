from flask import Flask , render_template , request , jsonify
import requests
import time

app = Flask(__name__)
API = "sec_XPTc23DgFiNZoQEyyR1Dhk1jVOyQBHJ0"
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get",methods = ["GET","POST"])
def chat():
    msg = request.form['msg']
    input = msg
    return get_chat_response(input)

def get_chat_response(text:str):
    headers = {
        'x-api-key': API,
        "Content-Type": "application/json",
    }

    data = {
        'sourceId': "cha_st6yE6PEKPjkqbE7MnCur",
        'messages': [
            {
                'role': "user",
                'content': str(text),
            }
        ]
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['content']
    else:
        print('Error:', response.text)
        return str(response.status_code)
        
        
        
            
if __name__ == "__main__":
    app.run()