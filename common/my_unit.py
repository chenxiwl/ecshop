import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MyUnit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/ecshop/admin/privilege.php?act=login")

    def tearDown(self):
        self.driver.close()

    def login_ecshop(self):
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='进入管理中心']").send_keys(Keys.ENTER)
        time.sleep(3)
        return self.driver
        # 断言缓一缓