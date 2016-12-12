import os, sys
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
import requests
import auxFunctions as afn

def Check_MageGame():
    dontcare = ['Cottonopolis: A Dream of Industry and Wonder','Mage 2054 (oWoD)']
    url = 'http://www.rpol.net/?gn=&gm=&gs=mage&sa=1&rp=1&af_general=1&af_mature=1&af_adult=1&af_sowner=1&match=all&sort=alphabetical&search=search'
    soup = afn.GetSoup(url)
    tr_v0 = soup.find_all('tr')
    tr_v1 = [tr for tr in tr_v0 if tr.get('id')]
    title_v = [str(tr.find('a').text) for tr in tr_v1]
    newGames = [title for title in title_v if title not in dontcare]
    # newGames.append('testgame')
    # newGames.append('anothertestgame')
    if len(newGames)!=0:
        gameString = '\"%s\"' %newGames[0]
        for game in newGames[1:]:
            gameString += ', \"%s\"' %game
        text = 'New game(s) available: %s<br>Check at this <a href=\'%s\'> link </a>' %(gameString,url)
        afn.SendMail('porziodavide@gmail.com','New available games at RPoL',text)
