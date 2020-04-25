import requests 
from bs4 import BeautifulSoup 
import json
from io import StringIO





def check():
    page = requests.get('https://www.webnovel.com/apiajax/chapter/GetChapterList?_csrfToken=null&bookId=15614995705203305')
    contents = page.json()
    return(contents['data']['bookInfo']['newChapterIndex'])



def insult():
    page = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    contents = page.json()
    return(contents["insult"])

def advice():
    page = requests.get('https://api.adviceslip.com/advice')
    contents = page.json()
    return(contents["slip"]["advice"])

def define(word: str):
    page=requests.get(f'https://owlbot.info/api/v4/dictionary/{word}',headers={'Authorization':'Token 6489c9ae10357d2f1175545c11f5e7a8570d835f'})
    contents = page.json()
    i=1
    meaning=StringIO()
    for de in contents['definitions']:
        meaning.write(str(i)+'. ('+de['type']+') '+de['definition']+'\n')
        i+=1
    return(meaning.getvalue())

def rate(country:str):
    page=requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    contents = page.json()
    return('1 USD = '+str(contents['rates'][country])+f' {country}')
