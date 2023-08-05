from flask import Flask, render_template, request
import requests
import datetime
from dotenv import load_dotenv
import os
import supabase 

load_dotenv()

#Supabase info
key = os.getenv('KEY')
url = os.getenv('LINK')


sup = supabase.create_client(url, key)
app = Flask(__name__)

#Query oer cercare e confermare la presenza dell'account negli utenti
def checkAccount(email:str,password:str):
    data = sup.table("users").select(("mail,password")).eq("mail",email).eq("password",password).execute()

    if len(data.data) == 1:
        return True
    

def checkPrenotazioni():
    pass  

#Index
@app.route('/')
def index():
    return render_template('index.html')

#-----Login-----
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if checkAccount(username,password):
            #Account esistente esito POSIITIVO
            return render_template('login.html', is_authenticated=True, message="Ok, va tutto bene")
        else:
            #Account non esistente esito NEGATIVO
            return render_template('login.html', is_authenticated=False, message="Credenziali non valide")
    else:
        return render_template('login.html')


@app.route('/addPrenotazione', methods=['GET', 'POST'])
def addPrenotazione():

    if request.method == 'POST':
        idCampo = int(request.form['campo'])

        data_str = request.form['data'] #Questa data viene fornita con un formato sbagliato quindi cambio il formato
        data = datetime.datetime.strptime(data_str, '%Y-%m-%d')

        print(data)

        #orarioInizio = request.form['orario_inizio']
        #cognome = request.form['cognome']

        # Stampa i dati ricevuti dal form a console
        print("ID Campo:", str(idCampo))
        #print("Data:", str(data))
        #print("Orario di Inizio:", str(orarioInizio))
        #print("Cognome:", str(cognome))

        # Resto del codice per gestire la prenotazione

        return render_template("addPrenotazione.html")
    else:
        return render_template("addPrenotazione.html")



if __name__ == '__main__':
    app.run()