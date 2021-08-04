class HomePage:

    # HomePage  
    PORTAL_BUTTON = '//*[class="elementor elementor-344""]'    

    def __init__(self,driver):
        self.driver=driver   

    def clickPortal(self):        
        self.driver.find_element_by_xpath(self.PORTAL_BUTTON).click()