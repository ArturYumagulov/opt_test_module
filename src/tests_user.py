from settings import SITE_URL, DRIVER_PATH
from browser import OptTest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


superuser = "TEST_SELENIUM"
superuser_pass = "@Zico19021991"
phone = "+72222222222"
pic = "C:\\Users\\YumagulovA\\Desktop\\pic.jpg"
mail = "test@bot.ru"
password = "password"


class TestOptUserReg(OptTest):

    def test_register(self):
        self.open(SITE_URL)
        self.driver.find_element_by_xpath('//*[@id="sticky-wrapper"]/div/div/div/div[4]/div/div[2]/a/div').click()
        self.driver.find_element_by_name("REGISTER[PERSONAL_PHONE]").send_keys(phone)
        self.driver.find_element_by_name("REGISTER[EMAIL]").send_keys(mail)
        self.driver.find_element_by_name("REGISTER[PERSONAL_CITY]").send_keys("Kazan")
        self.driver.find_element_by_name("UF_INN").send_keys("000000000")
        self.driver.find_element_by_name("UF_ADR_FACT").send_keys("Kazan")
        self.driver.find_element_by_name("REGISTER[NAME]").send_keys("Test_user")
        self.driver.find_element_by_name("UF_DOC_FILES[]").send_keys(pic)
        self.driver.find_element_by_name("REGISTER[PASSWORD]").send_keys(password)
        self.driver.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").send_keys(password)
        self.driver.find_element_by_name("register_submit_button").click()
        text = self.driver.find_element_by_xpath('/html/body/section/div/div/div/p[3]').text
        assert text == "Вы успешно зарегистрировались. Ваша учетная запись будет активирована после проверки данных", \
            "Регистрация не удалась"

    def test_del_user(self):
        self.open(f"{SITE_URL}bitrix/admin/")
        self.driver.find_element_by_name("USER_LOGIN").send_keys(superuser)
        self.driver.find_element_by_name("USER_PASSWORD").send_keys(superuser_pass)
        self.driver.find_element_by_name("Login").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("global_menu_settings").click()
        time.sleep(5)
        self.driver.execute_script('window.scroll(0, 0)')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="_global_menu_settings"]/div[3]').click()
        self.driver.find_element_by_xpath('//*[@id="_global_menu_settings"]/div[3]/div[2]/div[1]').click()
        self.driver.find_element_by_id("tbl_user_search").send_keys(phone[1:])
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(()))
        self.driver.find_element_by_xpath('//*[@id="tbl_user_table"]/tbody/tr[2]/td[1]').click()
        self.driver.find_element_by_id('grid_remove_button_control').click()
        self.driver.find_element_by_id('tbl_user-confirm-dialog-apply-button').click()


if __name__ == '__main__':
    x = TestOptUserReg()
    x.test_register()

