from selenium.webdriver.common.by import By
class Popular:
    def __init__(self,driver):
        self.driver=driver
    def navigate_popular_page(self):
        self.driver.find_element(By.XPATH,"//a[text()='Popular']").click()
    def movieslist_movie1(self):
        return self.driver.find_element(By.XPATH,"//img[@alt='Venom']")
    def movieslist_movie2(self):
        return self.driver.find_element(By.XPATH,"//img[@alt='Snake Eyes: G.I. Joe Origins']")
    def movieslist_movie3(self):
        return self.driver.find_element(By.XPATH,"//img[@alt='Luca']")
    def movieslist_movie4(self):
        return self.driver.find_element(By.XPATH,"//img[@alt='The Amazing Spider-Man']")