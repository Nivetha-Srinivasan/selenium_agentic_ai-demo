from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run_login_test():
    try:
        driver = webdriver.Chrome()
        driver.get("https://github.com/login")

        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.ID, "login").click()

        time.sleep(2)
        assert "Dashboard" in driver.page_source
        print("✅ Login test passed")
        driver.quit()
        return True

    except Exception as e:
        print("❌ Login test failed:", e)
        return False
