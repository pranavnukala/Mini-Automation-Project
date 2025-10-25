from pages.accounts_page import Account_page
import pytest
def test_accounts_page(logged_in_driver):
    driver=logged_in_driver
    account3=Account_page(driver)
    account3.profile_click()
    assert account3.membership_head_check().is_displayed()
    assert account3.membership_username_check().is_displayed()
    assert account3.membership_password_check().is_displayed()
    assert account3.plan_para_check().is_displayed()
    assert account3.plan_details_check().is_displayed()
    assert account3.logout_btn_check().is_displayed()
    assert account3.logout_btn_click()=="https://qamoviesapp.ccbp.tech/login"