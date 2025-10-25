from pages.Login_page import Login
import pytest
login_data=[
      ("", "", "error", "Username or password is invalid"),
      ("", "rahul@2021", "error", "Username or password is invalid"),
      ("rahul", "", "error", "Username or password is invalid"),
      ("rahul","rahul@2021", "success", "https://qamoviesapp.ccbp.tech/login")
]
@pytest.mark.parametrize("new_user,new_password,result_type,expected",login_data)
def test_login(setup,new_user,new_password,result_type,expected):
      driver=setup
      login=Login(driver)
      assert login.logotest().is_displayed()
      assert login.login_heading_test()=="Login"
      assert  login.username_label_test()=="USERNAME"
      assert  login.password_label_test()=="PASSWORD"
      assert login.check_loginbtn()=="Login"
      login.enter_username(new_user)
      login.enter_password(new_password)
      login.loginbtn_click()
      if(result_type=="success"):
            print("login Successfully")
            assert login.valid_login()==expected
      elif(result_type=="error"):
            print("Login Not Successful")
            assert expected in login.invalid_login()