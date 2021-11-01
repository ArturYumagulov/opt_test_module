import openpyxl as xl
from settings import *


def excel_reader(file_obj: str, sheet_name: str) -> list:
    """Функция чтения файла для передачи в модуль инициализации БД"""

    result = []
    wb = xl.load_workbook(file_obj)
    sheet = wb[sheet_name]
    for rows in sheet:
        lst = []
        for i in rows:
            if i.value is None:
                i = "н/д"
                lst.append(i)
            else:
                lst.append(i.value)
        result.append(tuple(lst))
    return result


if __name__ == '__main__':
    print(excel_reader(DATA_FILE_PATH, DATA_FILE_SHEET_NAME))