from selenium.webdriver.common.by import By
class Account_page:
    def __init__(self,driver):
        self.driver=driver
    def profile_click(self):
        return self.driver.find_element(By.CLASS_NAME,"avatar-button").click()
    def membership_head_check(self):
        return self.driver.find_element(By.CLASS_NAME,"membership-heading")
    def membership_username_check(self):
        return self.driver.find_element(By.CLASS_NAME,"membership-username")
    def membership_password_check(self):
        return self.driver.find_element(By.CLASS_NAME,"membership-password")
    def plan_para_check(self):
        return self.driver.find_element(By.CLASS_NAME,"plan-paragraph")
    def plan_details_check(self):
        return self.driver.find_element(By.CLASS_NAME,"plan-details")
    def logout_btn_check(self):
        return self.driver.find_element(By.CLASS_NAME,"logout-button")
    def logout_btn_click(self):
        self.driver.find_element(By.CLASS_NAME,"logout-button").click()
        url=self.driver.current_url
        return url