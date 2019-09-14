#!/usr/bin/python3
import time

import requests
import bs4

def translate(atext,fromlang,tolang):
    """Returns the translation using google translate
    you must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default

    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?
    """
    rtext=""
    
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    url = base_link % (tolang, fromlang, atext)
    print(url)
    headers={'Accept-Charset': 'utf-8'}
    r = requests.get(url,headers=headers)
    content = r.content.decode('utf-8')

    if r.status_code != 200:
        print("ERROR")
        print(r.status_code)
        print(r.headers)
        print("content",content)
        time.sleep(1)
    else:
        soup = bs4.BeautifulSoup(content,'html.parser')
        # print(soup) # div class="t0"
        res=soup.find("div",attrs={"class":"t0"})
        # print("res:",res)
        print("res.text:",res.text)
        rtext=res.text
    return rtext



def translate_wrapper(atext):
    """
    Takes a list of phrases
    """
    print("translating:",atext)
    res=""
    res=translate(atext,"pl","fr")
    time.sleep(0.5)
    print("translation:",res)
    return res
