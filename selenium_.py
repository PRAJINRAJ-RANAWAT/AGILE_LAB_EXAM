from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

username = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)

password = driver.find_element(By.ID, "password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

message = wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

assert "You logged into a secure area!" in message.text

print("Login successful")


driver.quit()