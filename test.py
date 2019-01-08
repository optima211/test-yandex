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

    def test_02(self):
        driver = self.driver
        print("1")
        driver.find_element_by_link_text("Картинки").click()
        print("2")
        time.sleep(2)
        st = driver.current_url
        # print(st)
        if st == "https://yandex.ru/images/":
            print("step")
            input_field = driver.find_element_by_class_name('cl-teaser__link').click()
            time.sleep(2)
            img1 = driver.current_url
            # print(img1)
            input_fields = driver.find_element_by_class_name('layout__nav__right').click()
            img2 = driver.current_url
            time.sleep(2)
            # print(img2)
            if img1!=img2:
                input_fields = driver.find_element_by_class_name('layout__nav__left').click()
                time.sleep(2)
                if img1==driver.current_url:
                    print("step2")
                else:
                    print("first image is modify!")
            else:
                print("image is not modify!")
        else:
            print("page image is not correct!")












    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()