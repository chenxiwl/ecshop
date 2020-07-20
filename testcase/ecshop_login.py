from selenium.webdriver.common.by import By

from common.my_unit import MyUnit

class EcshopLogin(MyUnit):

    def test_login(self):
        """登录ecshop"""
        driver=self.login_ecshop()
        driver.switch_to.frame("header-frame")
        sj_result=driver.find_element(By.CSS_SELECTOR,"a[href='privilege.php?act=logout']").text
        self.assertEqual(sj_result,'退出')