# -*- coding: utf-8 -*-
import datetime
import requests
from bs4 import BeautifulSoup
from project import const, db
from project.models.fensi import FenSi

def get_fen_count_by_brand(**params):
    now = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    today = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
    r = requests.get(params['url'])
    soup = BeautifulSoup(r.text, "lxml")
    times = 0
    while soup.find(id="followCount") is None:
        r = requests.get(params['url'])
        soup = BeautifulSoup(r.text, "lxml")
        if times == 10 :
            break
        times = times + 1
    if times < 10 :
        count = soup.find(id="followCount").attrs['value']
    else :
        count = soup.find(class_="shop_profile_extra").text.split("\n")[2].split(u"万")[0]

    db.session.add(FenSi(company= params['company'], count=count, updated=today, html=soup.find(class_="shop_profile_extra").text.split("\n")[2] or r.text))
    db.session.commit()
