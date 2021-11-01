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


# def run(product):
#     x = OptTest()
#     x.open(SITE_URL)
#     try:
#         x.search(product.article)
#         link = x.get_search_link()
#         try:
#             x.search_warehouse(link)
#             result = Results(datetime.datetime.now(), product.group, product.name, "не проводилось", product.article,
#                              'да', product.catalog_number, "не проводилось")
#             res.add(result)
#             res.commit()
#         except NoSuchElementException:
#             result = Results(datetime.datetime.now(), product.group, product.name, "не проводилось", product.article,
#                              'нет', product.catalog_number, "не проводилось")
#             res.add(result)
#             res.commit()
#     except IndexError:
#         result = Results(datetime.datetime.now(), product.group, product.name, "не проводилось", product.article,
#                          'нет', product.catalog_number, "не проводилось")
#         res.add(result)
#         res.commit()
#     x.close_browser()


def new_run(product):
    x = OptTest()
    result_dict = x.init(product.article)
    print(result_dict)
    result = Results(datetime.datetime.now(), product.group, product.name, "не проводилось", product.article, 'да',
                     product.catalog_number, "не проводилось", result_dict[product.article]["PRT"],
                     result_dict[product.article]["TR"])
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
    version_control(products, statuses)
