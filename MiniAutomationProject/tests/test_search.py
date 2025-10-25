from pages.search_page import Search_page,MovieDetailsPageTest
import pytest
search_data=[
    ("Luca","success","1"),
    ("maharshi","error","Your search for maharshi did not find any matches.")
]
@pytest.mark.parametrize("movie_name,result_type,expected",search_data)
def test_search(logged_in_driver,movie_name,result_type,expected):
    driver=logged_in_driver
    search=Search_page(driver)
    search.search_btnclick()
    search.input_test(movie_name)
    if(result_type=="success"):
        assert search.valid_search()==1
    elif(result_type=="error"):
        assert search.invalid_search()==expected
def test_movies_list_page(logged_in_driver):
    driver=logged_in_driver
    movies_test=MovieDetailsPageTest(driver)
    assert movies_test.top_head_test().is_displayed()
    assert movies_test.trending_head_test()=="Trending Now"
    assert movies_test.original_head_test()=="Originals"
    assert movies_test.movieslist_movie1().is_displayed()
    assert movies_test.contactus_head_test().is_displayed()
    assert movies_test.icons_check().is_displayed()
    movies_test.nav_popular_test()
    movies_test.movies_list_check().is_displayed()