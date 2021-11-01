from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import *

from db import Base, Product
from data import excel_reader


engine = create_engine(DATABASE, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()


for product in excel_reader(BRANDS, BRANDS_SHEET_NAME):
    """Чтание из файла и запись данных в БД"""

    p = Product(product[0], product[1], product[3], product[4])
    s.add(p)
s.commit()
