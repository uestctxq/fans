# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 下午10:47
# @Author  : xiaoqingtang
# @Site    : 
# @File    : fensi.py

from project import db
from sqlalchemy import PrimaryKeyConstraint

class FenSi(db.Model):
    __tablename__ = 'shop_fensi'

    id = db.Column(db.Integer)
    company = db.Column(db.String(200))
    count = db.Column(db.Integer)
    updated = db.Column(db.DateTime)
    html = db.Column(db.Text)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )

    def __repr__(self):
        return '<shop_fensi id:{} company:{} count:{} >'.format(self.id, self.company, self.count)

    def getCompanyData(self, company):
        """
        :param company:
        :return:
        """
        return FenSi.query.filter_by(company=company).all()