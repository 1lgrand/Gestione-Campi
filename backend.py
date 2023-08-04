from flask import Flask,render_template
import requests
from dotenv import load_dotenv
import os
import supabase as sb

load_dotenv()


key = os.getenv('KEY')
url = os.getenv('LINK')

sup = sb.create_client(url, key)


app = Flask(__name__)

def checkAccount(email:str,password:str):
    data = sup.table("users").select(("mail,password")).eq("mail",email).eq("password",password).execute()

    if len(data.data) == 1:
        return True
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()