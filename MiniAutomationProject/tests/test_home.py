import pytest
from pages.home_page import Home,HeaderSectionTest
def testing_home(logged_in_driver):
    driver=logged_in_driver
    home=Home(driver)
    assert home.top_head_test().is_displayed()
    assert home.trending_head_test()=="Trending Now"
    assert home.original_head_test()=="Originals"
    assert home.movieslist_movie1().is_displayed()
    assert home.contactus_head_test().is_displayed()
    assert home.icons_check().is_displayed()
    header=HeaderSectionTest(driver)
    assert header.nav_home_uicheck().is_displayed()
    assert header.nav_popular_uicheck().is_displayed()
    assert header.nav_home_test()=="https://qamoviesapp.ccbp.tech/"
    assert header.nav_popular_test()=="https://qamoviesapp.ccbp.tech/popular"
    assert header.accountpage_navigate_test()=="https://qamoviesapp.ccbp.tech/account"
