from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find the field for entering a wrong login or an email address 
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Enter a wrong login or an email address 
        login_elem.send_keys(username)

        # Find the field for entering a wrong password 
        pass_elem = self.driver.find_element(By.ID, "password")

        # Enter a wrong password 
        pass_elem.send_keys(password)

        # Find the button "Sign in"
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate a click of the left mouse button 
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title