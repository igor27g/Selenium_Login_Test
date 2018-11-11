from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginForm():

    def test(self):
        baseUrl = "https://www.udemy.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        mailLinkForm = driver.find_element(By.XPATH, "//div[@class='dropdown dropdown--login ud-component--header-v6--login-button hidden-xs hidden-xxs']//div//button[@type='button'][contains(text(),'Zaloguj się')]")
        mailLinkForm.click()

        time.sleep(5)

        userLogin = driver.find_element(By.XPATH, "//input[@placeholder='E-mail']")
        userLogin.send_keys("usernametest@mail.com")

        time.sleep(5)

        userPassword = driver.find_element(By.XPATH, "//input[@id='id_password']")
        userPassword.send_keys("userpasswordtest")

        time.sleep(5)

        loginButton = driver.find_element(By.XPATH, "//input[@id='submit-id-submit']")
        loginButton.click()

        



ff = LoginForm()
ff.test()



