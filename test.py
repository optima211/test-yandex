import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.yandex.ru')

    def test_01_yandex_search(self):
        driver = self.driver
        input_field = driver.find_element_by_id('text')
        input_field.send_keys('тензор')
        time.sleep(2)
        input_field.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        driver.find_element_by_class_name('suggest2__content')
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)
        titles = driver.find_elements_by_class_name('r')
        for title in titles:
            assert "tensor.ru" in title.text.lower()
            time.sleep(4)

    def test_02_yandex_image(self):
        driver = self.driver
        driver.find_element_by_link_text("Картинки").click()
        time.sleep(2)
        st = driver.current_url
        if st == "https://yandex.ru/images/":
            driver.find_element_by_class_name('cl-teaser__link').click()
            time.sleep(2)
            img1 = driver.current_url
            driver.find_element_by_class_name('layout__nav__right').click()
            img2 = driver.current_url
            time.sleep(2)
            if img1 != img2:
                driver.find_element_by_class_name('layout__nav__left').click()
                time.sleep(2)
                if img1 != driver.current_url:
                    print("first image is modify!")
            else:
                print("image is not modify!")
        else:
            print("page image is not correct!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
