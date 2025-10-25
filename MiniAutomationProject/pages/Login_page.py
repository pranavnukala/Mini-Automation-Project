from selenium.webdriver.common.by import By
class Login:
    def __init__(self,driver):
        self.driver=driver
    def logotest(self):
        return self.driver.find_element(By.CLASS_NAME,"login-website-logo")
    def login_heading_test(self):
        return self.driver.find_element(By.CLASS_NAME,"sign-in-heading").text
    def username_label_test(self):
        return self.driver.find_element(By.XPATH,"//label[text()='USERNAME']").text
    def password_label_test(self):
        return self.driver.find_element(By.XPATH,"//label[text()='PASSWORD']").text
    def check_loginbtn(self):
        return self.driver.find_element(By.CLASS_NAME,"login-button").text
    def enter_username(self,new_user):
        self.driver.find_element(By.ID,"usernameInput").send_keys(new_user)
    def enter_password(self,new_password):
        self.driver.find_element(By.ID,"passwordInput").send_keys(new_password)
    def loginbtn_click(self):
        self.driver.find_element(By.CLASS_NAME,"login-button").click()
    def invalid_login(self):
        return self.driver.find_element(By.XPATH,"//p[text()='Username or password is invalid']").text
    def valid_login(self):
        url=self.driver.current_url
        return url
 
