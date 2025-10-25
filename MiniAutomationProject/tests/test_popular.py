from pages.popular_page import Popular
import pytest
def test_popular(logged_in_driver):
     driver=logged_in_driver
     popular=Popular(driver)
     popular.navigate_popular_page()
     assert popular.movieslist_movie1().is_displayed()
     assert popular.movieslist_movie2().is_displayed()
     assert popular.movieslist_movie3().is_displayed()
     assert popular.movieslist_movie4().is_displayed()