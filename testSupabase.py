import supabase 
from dotenv import load_dotenv
import os
load_dotenv()


key = os.getenv('KEY')
url = os.getenv('LINK')

sup = supabase.create_client(url, key)

def checkAccount(email:str,password:str):
    data = sup.table("users").select(("mail,password")).eq("mail",email).eq("password",password).execute()

    if len(data.data) == 1:
        return True


checkAccount("admin","dada")