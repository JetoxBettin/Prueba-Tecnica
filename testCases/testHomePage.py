import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.homePage import HomePage


class Test_Home_Page:

    URL = 'https://www.choucairtesting.com/'       
    TITLE = 'empleos testing'

    def test_homePage(self, setup):      
        self.driver = setup
        self.driver.get(self.URL)
        self.hp=HomePage(self.driver)        
        self.hp.clickEmployess()
        print(self.driver.title)               
        if self.TITLE in self.driver.title:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.quit()
            assert False

    def test_navigate(self, setup):
        self.driver = setup
        self.driver.get("https://www.selenium.dev/downloads/")
        self.driver.quit()
        assert True        
