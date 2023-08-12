from flask import Flask, render_template, request
import requests
import datetime
from dotenv import load_dotenv
import os
import supabase 
import queryes

load_dotenv()

#Supabase info
key = os.getenv('KEY')
url = os.getenv('LINK')


sup = supabase.create_client(url, key)
app = Flask(__name__)

    

def checkPrenotazioni(dict):

    sup.table("prenotazioni").insert(dict).execute()


@app.route('/', methods=['GET', 'POST'])
def addPrenotazione():

    if request.method == 'POST':
        nGiocatori = int(request.form['campo'])

        data_str = request.form['data'] #Questa data viene fornita con un formato sbagliato quindi cambio il formato
        data = datetime.datetime.strptime(data_str, '%Y-%m-%d').date()

        orarioInizio = request.form['orario_inizio']
        cognome = request.form['cognome']

        # Stampa i dati ricevuti dal form a console
        print("nGiocatori:", str(nGiocatori))
        print("Data:", str(data))
        print("Orario di Inizio:", str(orarioInizio))
        print("Cognome:", str(cognome))

        # Resto del codice per gestire la prenotazione

        ora_fine = datetime.datetime.strptime(orarioInizio,'%H:%M') + datetime.timedelta(hours=1)

        campo = queryes.checkDisponibilitàCalcio(data,orarioInizio,nGiocatori)

        if campo != -1:

            prenotazione = {
            "idCampo": campo,
            "data":str(data),
            "ora_inizio":str(orarioInizio),
            "ora_fine": str(ora_fine),
            "cognome":cognome
        }
            checkPrenotazioni(prenotazione)
        else:
            print("Tutti i campi sono occupati")

        return render_template("index.html")
    else:
        return render_template("index.html")



if __name__ == '__main__':
    app.run()