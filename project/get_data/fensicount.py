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
    count = soup.find(id="followCount").attrs['value']
    db.session.add(FenSi(company= params['company'], count=count, updated=today))
    db.session.commit()
