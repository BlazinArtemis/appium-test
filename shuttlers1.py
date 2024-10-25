import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options  # Import for Android automation options
import os
from appium.webdriver.common.appiumby import AppiumBy  # Import AppiumBy for locating elements
import time

class MobileAppTest(unittest.TestCase):
    def setUp(self):
        # Define the current directory and APK path
        CUR_DIR = os.path.dirname(os.path.abspath(__file__))
        APP = os.path.join(CUR_DIR, 'shuttlers.apk')  # Path to your APK

        # Define the Appium server URL
        APPIUM = 'http://localhost:4723/wd/hub'

        # Define Android-specific capabilities using UiAutomator2Options
        CAPS = {
            'platformName': 'Android',
            'deviceName': 'Pixel_7a',  # Name of the device/emulator
            'automationName': 'UiAutomator2',  # Using UiAutomator2 for Android
            'app': APP,  # Path to your APK file
            'udid': '33211JEHN05397',  # Unique device identifier (UDID)
            'newCommandTimeout': 3600,
            'ensureWebviewsHavePages': True,
            'nativeWebScreenshot': True,
            'connectHardwareKeyboard': True,
        }

        # Initialize the Appium driver with Android-specific options
        self.driver = webdriver.Remote(APPIUM, options=UiAutomator2Options().load_capabilities(CAPS))


    def test_login_flow(self):
            # Step 1: Click "Get Started"
            el1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Get Started")
            el1.click()

            # Step 2: Click "Skip"
            time.sleep(5)
            el2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Skip")
            el2.click()

            # Step 3: Click "Sign In" tab (Android UI Automator)
            el3 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Sign In")')
            el3.click()

            # Step 4: Click "Sign In" button
            # el4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign In")
            # el4.click()

            # Step 5: Fill in email field
            el5 = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
            el5.click()
            el5.send_keys("oluwaseyinexus137+refer1@gmail.com")

            # Step 6: Fill in the second email field
            # el6 = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")[1]
            # el6.click()
            # el6.send_keys("oluwaseyinexus137@gmail.com")

            # Step 7: Click "Proceed"
            el7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Proceed")
            el7.click()

            # Step 8: Fill in the password field
            el8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            el8.click()
            el8.send_keys("shuttlers")

            # Step 9: Click "Proceed"
            el9 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Proceed")
            el9.click()
            time.sleep(2)
    def tearDown(self):
            # Quit the Appium driver session after the test
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()