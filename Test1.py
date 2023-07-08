import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")
time.sleep(3)
driver.find_element(By.NAME,'field-keywords').send_keys("poco m2 pro")
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
driver.find_element(By.XPATH, "//span[normalize-space()='MI Poco M2 Pro (Two Shades of Black, 6GB RAM, 128GB Storage)']").click()
j=child=driver.window_handles[1]
driver.switch_to.window(j)
driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']").click()
time.sleep(3)
driver.find_element(By.ID,"attach-close_sideSheet-link").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@id='nav-cart-count']").click()
time.sleep(5)
print(driver.title)
driver.close()
driver.quit()
print("test completed")
