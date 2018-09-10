# -*- coding: utf-8 -*-

from project import app, const
from flask import render_template, request
from project.get_data.fensicount import get_fen_count_by_brand

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/print',methods=['GET','POST'])
def printer():
    if request.method=='GET':
        for k in const.COMPANY.keys():
            params = {}
            params['company'] = k
            params['url'] = const.COMPANY[k]
            get_fen_count_by_brand(**params)
        return render_template('print.html')

    return render_template('print.html')


