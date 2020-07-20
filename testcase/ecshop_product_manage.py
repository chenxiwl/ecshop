import random
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.my_unit import MyUnit

class EcshopProductManage(MyUnit):

    def test_product_add(self):
        """商品增加"""
        #登录
        driver=self.login_ecshop()
        #框架
        #进入框架：
        driver.switch_to.frame("menu-frame")
        driver.find_element(By.CSS_SELECTOR,"a[href='goods.php?act=list']").click()
        #退出框架
        driver.switch_to.default_content()
        driver.switch_to.frame("main-frame")
        driver.find_element(By.LINK_TEXT,"添加新商品").click()
        time.sleep(3)
        #添加新商品
        sn=random.randint(1000000000,9999999999)
        driver.find_element(By.NAME,"goods_name").send_keys("老北京布鞋"+str(sn))
        driver.find_element(By.NAME,"goods_sn").send_keys(str(sn))
        #下拉框处理
        sel=Select(driver.find_element(By.NAME,"cat_id"))
        sel.select_by_value("7")   #通过值选中
        #sel.select_by_index("4")   #通过下标选中
        #sel.select_by_visible_text("    充电器")   #通过文本选中
        price=driver.find_element(By.NAME,"shop_price")
        price.clear()
        price.send_keys("100")
        img=driver.find_element(By.NAME,"goods_img")
        img.clear()
        img.send_keys("E:\\login.png")
        driver.find_element(By.CSS_SELECTOR,"input[value=' 确定 ']").click()

    # @unittest.skip("删除用例不执行")
    # def test_product_delete(self):
    #     """商品删除"""
    #     # 登录
    #     driver=self.login_ecshop()
    #     # 框架
    #     driver.switch_to.frame("menu-frame")
    #     driver.find_element(By.LINK_TEXT, "商品列表").click()
    #     time.sleep(3)
    #     driver.switch_to.default_content()
    #     driver.switch_to.frame("main-frame")
    #     # 删除
    #     imgList = driver.find_elements(By.CSS_SELECTOR, "img[src='images/icon_trash.gif']")
    #     imgList[2].click()
    #     ale = driver.switch_to.alert
    #     ale.accept()