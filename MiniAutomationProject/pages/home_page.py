from selenium.webdriver.common.by import By
class Home:
    def __init__(self,driver):
        self.driver=driver
    def top_head_test(self):
        return self.driver.find_element(By.CLASS_NAME,"home-movie-heading")
    def trending_head_test(self):
        return self.driver.find_element(By.XPATH,"//h1[text()='Trending Now']").text
    def original_head_test(self):
        return self.driver.find_element(By.XPATH,"//h1[text()='Originals']").text
    def playbtn_test(self):
        return self.driver.find_element(By.CLASS_NAME,"home-movie-play-button").text
    def movieslist_movie1(self):
        return self.driver.find_element(By.CLASS_NAME,"poster")
    def contactus_head_test(self):
        return self.driver.find_element(By.CLASS_NAME,"contact-us-paragraph")
    def icons_check(self):
        return self.driver.find_element(By.CLASS_NAME,"footer-icons-container")
class HeaderSectionTest:
     def __init__(self,driver):
          self.driver=driver
     def website_logo_check(self): 
         return self.driver.find_element(By.CLASS_NAME,"login-website-logo")
     def nav_home_uicheck(self):
         return self.driver.find_element(By.XPATH,"//a[text()='Home']")
     def nav_popular_uicheck(self):
         return self.driver.find_element(By.XPATH,"//a[text()='Popular']")
     def nav_home_test(self):
         self.driver.find_element(By.XPATH,"//a[text()='Home']").click()
         return self.driver.current_url
     def nav_popular_test(self):
         self.driver.find_element(By.XPATH,"//a[text()='Popular']").click()
         return self.driver.current_url
     def accountpage_navigate_test(self):
         self.driver.find_element(By.CLASS_NAME,"avatar-button").click()
         return self.driver.current_url