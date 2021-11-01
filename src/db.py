from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import datetime


Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    uid = Column(Integer, primary_key=True)
    group = Column(String(255))
    name = Column(String(255))
    article = Column(String(50))
    catalog_number = Column(String(50))

    def __init__(self, group, name, article, catalog_num):
        self.group = group
        self.name = name
        self.article = article
        self.catalog_number = catalog_num


class Results(Base):
    __tablename__ = "result"

    uid = Column(Integer, primary_key=True)
    test_date = Column(DateTime, default=datetime.datetime.utcnow)
    group = Column(String(255))
    name = Column(String(255))
    result_name = Column(String(50))
    article = Column(String(50))
    result_article = Column(String(50))
    catalog_number = Column(String(50))
    result_catalog_num = Column(String(50))
    part_kom = Column(Integer)
    tran_zit = Column(Integer)

    def __init__(self, test_date, group, name, result_name, article, result_article, catalog_num, result_catalog_num,
                 part_kom, tran_zit):
        self.test_date = test_date
        self.group = group
        self.name = name
        self.result_name = result_name
        self.article = article
        self.result_article = result_article
        self.catalog_number = catalog_num
        self.result_catalog_num = result_catalog_num
        self.part_kom = part_kom
        self.tran_zit = tran_zit
