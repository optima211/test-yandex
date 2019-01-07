import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.yandex.ru')

    def test_01(self):
        driver = self.driver
        print("1\n")
        input_field = driver.find_element_by_id('text')
        print("2\n")
        input_field.send_keys('тензор')
        print("3-1\n")
        time.sleep(2)
        input_field.send_keys(Keys.ARROW_DOWN)
        print("3-2\n")
        time.sleep(2)
        input_fields = driver.find_element_by_class_name('suggest2__content')
        input_field.send_keys(Keys.ENTER)
        print("4\n")

        time.sleep(2)
        print("5\n")

        titles = driver.find_elements_by_class_name('r')
        for title in titles:
            assert "tensor.ru" in title.text.lower()
            time.sleep(4)
            # input_field = driver.find_element_by_link_text("Тензор — IT - компания").click()

            # input_field = driver.find_element_by_partial_link_text("tensor.ru").click()
            # input_field.send_keys(Keys.ENTER)
            # time.sleep(4)


    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()