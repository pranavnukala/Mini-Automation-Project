from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Search_page:
     def __init__(self,driver):
        self.driver=driver
     def search_btnclick(self):
         self.driver.find_element(By.CLASS_NAME,"search-empty-button").click()
     def input_test(self,movie_name):
         self.driver.find_element(By.ID,"search").send_keys(movie_name)
     def valid_search(self):
         self.driver.find_element(By.CLASS_NAME,"search-button").click()
         movies=WebDriverWait(self.driver,10).until(
             EC.visibility_of_all_elements_located((By.CLASS_NAME,"movie-icon-item"))
             )
         count=len(movies)
         return count
     def invalid_search(self):
         self.driver.find_element(By.CLASS_NAME,"search-button").click()
         return self.driver.find_element(By.CLASS_NAME,"not-found-search-paragraph").text
class MovieDetailsPageTest:
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
    def nav_popular_test(self):
         self.driver.find_element(By.XPATH,"//a[text()='Popular']").click()
    def movies_list_check(self):
         return self.driver.find_element(By.CLASS_NAME,"movie-image")

