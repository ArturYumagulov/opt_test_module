#!/usr/bin/env python3

import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import *
from browser import OptTest
from db import Product, Results

engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)
s = Session()
res = Session()
stat = Session()
statuses = s.query(Results).all()
products = s.query(Product).all()


def new_run(product):
    x = OptTest()
    result_dict = x.init(product.article)
    print(result_dict)
    prt = 0
    tr = 0

    for i in result_dict[product.article]:
        if i == "PRT" or i == "TR":
            prt += result_dict[product.article]["PRT"]
            tr += result_dict[product.article]["TR"]
        elif result_dict[product.article][i]["PRT"] == "null":
            pass
        elif result_dict[product.article][i]["PRT"] >= 0:
            prt += result_dict[product.article][i]["PRT"]
            tr += result_dict[product.article][i]["TR"]
    result = Results(datetime.datetime.now(), product.group, product.name, "не проводилось", product.article, 'да',
                     product.catalog_number, "не проводилось", prt,
                     tr)
    res.add(result)
    res.commit()


def version_control(products_list, statuses_list):
    st = [j.article for j in statuses_list]
    for i in products_list:
        if i.article == "н/д":
            pass
        elif i.article not in st:
            new_run(i)


if __name__ == '__main__':
    print("run...")
    version_control(products, statuses)
