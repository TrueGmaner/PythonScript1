import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# Наследуем наш класс от класса unittest.TestCase
class PythonOrgSearch(unittest.TestCase):
# Задаем веб-драйвер как поле класса PythonOrgSearch
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,  executable_path=r'C:\Users\alliw\Documents\chromedriver')
    def test_1(self): #проверяем на корректность подсчета
        self.driver.get("https://vk.com/")
        elemLogin = self.driver.find_element_by_xpath('//*[@id="index_email"]')
        sleep(2)
        elemLogin.send_keys('89165931657')
        elemPassword = self.driver.find_element_by_xpath('//*[@id="index_pass"]')
        sleep(2)
        elemPassword.send_keys('GermanPass')
        elemEnterButton = self.driver.find_element_by_xpath('//*[@id="index_login_button"]')
        sleep(2)
        elemEnterButton.click()
        sleep(5)
        elemFriendList = self.driver.find_element_by_xpath('//*[@id="l_fr"]/a/span')
        elemFriendList.click()
        sleep(2)
        elemCurrentFriendMessage = self.driver.find_element_by_xpath('//*[@id="friends_user_row109547849"]/div[3]/div[4]/a')
        elemCurrentFriendMessage.click()
        sleep(2)
        elemMessage = self.driver.find_element_by_xpath('//*[@id="mail_box_editable"]')
        elemMessage.send_keys('Сань хуй саси ')
        sleep(2)
        elemSend = self.driver.find_element_by_xpath('//*[@id="mail_box_send"]')
        elemSend.click()
        sleep(5)
# Запускаем тесты
if __name__ == '__main__':
    unittest.main()