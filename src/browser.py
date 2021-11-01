from selenium import webdriver
from settings import DRIVER_PATH, SITE_URL


class OptTest:
    """Класс тестирования"""

    def __init__(self):
        """Инициализация класса:
        опции для работы браузера в фоновом режиме,
        пределение драйвера браузера"""

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(DRIVER_PATH)

    def open(self, link: str):
        """Метод октытия ссылки"""

        self.driver.get(link)
        self.driver.execute_script("window.stop")

    def time(self, sec: int):
        """Таймер загрузки страницы"""

        self.driver.implicitly_wait(sec)

    def search(self, article: str):
        """Метод поиска:
        передача значения и клик по кнопке поиска"""

        self.driver.find_element_by_id("title-search-input").send_keys(article)
        self.driver.find_element_by_css_selector("#title-search > form > div > div > "
                                                 "div.cell.large-4.medium-4.small-2 > button").click()

    def close_browser(self):
        """Закрытые браузера"""

        self.driver.close()

    def get_search_links(self, article: str) -> dict:
        """Получение ссылок с результатами поиска:
        возвращает словарь с ссылками"""

        links = self.driver.find_elements_by_xpath('//*[@id="search_results_container_items"]/div/a')
        params = dict()
        if len(links) > 0:
            for ii in links:
                clear_link = ii.get_attribute("href")
                txt = ii.text.split("\n")
                links_dict = {"link": clear_link, "name": txt[-1], "article": txt[1], "brand": txt[0]}
                params[f"{links_dict['brand']} {links_dict['article']}"] = links_dict
                # params[article] = links_dict
            return params

    def get_search_link(self) -> str:
        """Получение ссылки с результатами поиска:
                возвращает ссылку"""

        link = self.driver.find_elements_by_xpath('//*[@id="search_results_container_items"]/div/a[1]')
        lnk = link[0].get_attribute('href')
        return lnk

    def search_warehouse(self, url: str) -> dict:
        """Поиск наличия на складе после нахождения нужного товара
        PRT: Парт-ком
        TR: Транзит
        """

        result_dict = {"PRT": 0, "TR": 0}
        self.open(url)
        if self.driver.current_url.split('=')[-1] == 'noname':
            result_dict["PRT"] = 'null'
            result_dict["TR"] = 'null'

        elif self.driver.current_url.split("/")[3] == 'detail':
            """Проверка ссылки с описанием товара"""
            product_list = self.driver.find_elements_by_class_name("brand_group_right_block")
            for i in product_list:
                data = i.text.split()
                if "PrT" in data:
                    result_dict["PRT"] += 1
                if "Свой" and "склад" in data:
                    result_dict["TR"] += 1
        elif self.driver.current_url.split("/")[3] == "manager-order":
            result_dict["PRT"] = 'null'
            result_dict["TR"] = 'null'
        else:
            self.stop_script()
        return result_dict

    def stop_script(self):
        """Остановка загрузки страницы"""
        self.driver.execute_script("window.stop()")

    def valid_search(self):
        products = self.driver.find_elements_by_class_name("brand_group_right_block")
        return products

    def init(self, article: str) -> dict:
        """Инициализатор"""

        res = {}
        new_res = {}
        result_dict = {"PRT": 0, "TR": 0}
        self.open(SITE_URL)
        self.search(article)

        if self.driver.current_url.split('/')[3] == 'search':
            """Проверка на наличие страницы с результатами поиска"""
            
            products = self.get_search_links(article)
            for i in products:
                res[i] = self.search_warehouse(products[i]["link"])
            new_res[article] = res
            self.close_browser()
            # return new_res

        elif self.driver.current_url.split('/')[3] == 'detail':
            """Проверка  на наличие страницы с вариантами"""

            prod = self.valid_search()

            for i in prod:
                data = i.text.split()
                if "PrT" in data:
                    result_dict["PRT"] += 1
                if "Свой" and "склад" in data:
                    result_dict["TR"] += 1
            new_res[article] = result_dict
            self.close_browser()
            # return new_res

        elif self.driver.current_url.split("/")[3] == "manager-order":
            result_dict["PRT"] = 'null'
            result_dict["TR"] = 'null'
            new_res[article] = result_dict
            self.close_browser()
        return new_res


if __name__ == '__main__':
    x = OptTest()
    print(x.init("w 914/2"))
