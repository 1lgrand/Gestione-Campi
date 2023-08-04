from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import supabase 

load_dotenv()


key = os.getenv('KEY')
url = os.getenv('LINK')

sup = supabase.create_client(url, key)


app = Flask(__name__)

def checkAccount(email:str,password:str):
    data = sup.table("users").select(("mail,password")).eq("mail",email).eq("password",password).execute()

    if len(data.data) == 1:
        return True
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if checkAccount(username,password):
            # L'account esiste e l'utente è autenticato con successo
            return render_template('login.html', is_authenticated=True, message="Ok, va tutto bene")
        else:
            # Le credenziali non sono valide o l'account non esiste
            return render_template('login.html', is_authenticated=False, message="Credenziali non valide")
    else:
        return render_template('login.html')



if __name__ == '__main__':
    app.run()