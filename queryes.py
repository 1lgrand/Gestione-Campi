import supabase 
from dotenv import load_dotenv
import os
load_dotenv()


key = os.getenv('KEY')
url = os.getenv('LINK')

sup = supabase.create_client(url, key)

#Query oer cercare e confermare la presenza dell'account negli utenti
def checkAccount(email:str,password:str):
    data = sup.table("users").select("mail,password").eq("mail",email).eq("password",password).execute()

    if len(data.data) == 1:
        return True
    

def checkDisponibilitàCalcio(data:str, ora_inizio:str, nGiocatori:int):

    dataCampi = sup.table("campi").select("id,nGiocatori,disponibile").eq("nGiocatori", nGiocatori).eq("disponibile", True).execute().data

    data_prenotazioni = sup.table("prenotazioni").select("idCampo,data,ora_inizio").eq("data", data).eq("ora_inizio", ora_inizio).execute().data

    idCampi = [campo['id'] for campo in dataCampi]

    if data_prenotazioni:
        for prenotazione in data_prenotazioni:
            if prenotazione['idCampo'] in idCampi:
                idCampi.remove(prenotazione['idCampo'])

    if len(idCampi) == 0:
        print("[ERRORE] Non ci sono campi disponibili")
        return -1
    else:
        return idCampi[0]





