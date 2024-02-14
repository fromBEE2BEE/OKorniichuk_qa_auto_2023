import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Create the object for browser management  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Load the page: https://github.com/login 
    driver.get("https://github.com/login")

    # Find the field for entering a wrong login or an email address 
    login_elem = driver.find_element(By.ID, "login_field")

    # Enter a wrong login or an email address 
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # Find the field for entering a wrong password      
    pass_elem = driver.find_element(By.ID, "password")

    # Enter a wrong password 
    pass_elem.send_keys("wrong password")

    # Find the button "Sign in"
    btn_elem = driver.find_element(By.NAME, "commit")

    # Emulate a click of the left mouse button    
    btn_elem.click()
    
    # Check that the page name where we are on is correct          
    assert driver.title == "Sign in to GitHub · GitHub"

    # Close the browser 
    driver.close()


@pytest.mark.ui
def test_search_cargo_positive():
    # Create the object for browser management 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Load the  page: https://novaposhta.ua 
    driver.get("https://novaposhta.ua")

    # Find the proper field for entering the correct invoice number    
    cargo_number_elem = driver.find_element(By.ID, "cargo_number")
    
    # Fill in the correct invoice number 
    cargo_number_elem.send_keys('20450857971424')
    
    # Find the button that closes an advertisement 
    adv_btn = driver.find_element(By.XPATH, ".//div[@id='popup_info']//div[@class='header']//i[text()='закрыть']")

    # Emulate a click of the left mouse button
    adv_btn.click()
    
    # Find the  'submit' button
    btn_elem = driver.find_element(By.XPATH, ".//div[@id='wrapper']//input[@name='' and @type='submit']")
   
    # Emulate a click of the left mouse button
    btn_elem.click()
    
    # Find the message with the text: 'Зрозуміло'
    inform_elem = driver.find_element(By.XPATH, ".//button[@class='button v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default']//span[@class='v-btn__content']")
   
    # Emulate a click of the left mouse button
    inform_elem.click()
   
    # Check that the page name where we are on is correct  
    assert driver.title == 'Трекінг Нова пошта - відстежити посилку, відслідковувати ТТН'
    
    # Close the browser
    driver.close()



