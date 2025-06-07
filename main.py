import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Load BrowserStack credentials from environment variables
USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

# Scalelup login credentials
EMAIL = "Sophiemae802@gmail.com"
PASSWORD = "1Adeniran."

# BrowserStack capabilities
desired_cap = {
    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': 'latest',
    'name': 'Scalelup Bot Session',
    'build': 'Scalelup-Auto-Bot',
}

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

try:
    # Open login page
    driver.get("https://scalelup.com/login")
    time.sleep(5)

    # Fill in login form
    driver.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(8)

    # Navigate to discover page
    driver.get("https://scalelup.com/discover")
    time.sleep(8)

    # Loop through ads
    while True:
        try:
            # Wait for ad timer (adjust if needed)
            time.sleep(22)

            # Click ❤️ love button
            love_buttons = driver.find_elements(By.CLASS_NAME, "post-reaction-button")
            for button in love_buttons:
                if "❤️" in button.text:
                    button.click()
                    break

            time.sleep(2)

            # Click "Show Next Post" if exists
            next_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Show Next Post')]")
            next_btn.click()
            time.sleep(5)
        except Exception as e:
            print("No more posts or error occurred:", e)
            break

finally:
    driver.quit()
