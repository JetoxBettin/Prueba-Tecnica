class HomePage:

    # HomePage  
    EMPLOYEES_BUTTON = '//*[@class="menu-item menu-item-type-post_type menu-item-object-page menu-item-550"]'    

    def __init__(self,driver):
        self.driver=driver   

    def clickEmployess(self):        
        self.driver.find_element_by_xpath(self.EMPLOYEES_BUTTON).click()
    