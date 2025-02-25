# -*- coding: utf-8 -*-
import time
import os
import logging

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

logging.basicConfig(level=logging.INFO)

def initial_driver():
    global driver

    options = UiAutomator2Options()
    desired_caps = {
        "platformName": "android",
        "automationName": "UiAutomator2",
        "platformVersion": "14", 
        "deviceName": "R5CTB15D3GM",
        "appPackage": "hko.MyObservatory_v1_0",
        "appActivity": "hko.homepage3.HomepageActivity",
        "udid": "R5CTB15D3GM"
    }
    logging.info(desired_caps)
    appium_host = 'http://127.0.0.1:4724/wd/hub'

    try:
        driver = WebDriver(appium_host, options=options.load_capabilities(desired_caps))
        logging.info("connect success")
    except Exception as e:
        logging.error(f"connect fail: {e}")
        raise

def skip_initial_app_page(driver):
    """
    Skip app permission and initial page
    """

    locators = {
        "btn_agree": "//android.widget.Button[@resource-id='hko.MyObservatory_v1_0:id/btn_agree']",
        "ok_btn": "//android.widget.Button[@resource-id='android:id/button1']",
        "permission_allow_one_time_button": "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_one_time_button']",
        "allow_always_radio_button": "//android.widget.RadioButton[@resource-id='com.android.permissioncontroller:id/allow_always_radio_button']",
        "back_page_btn": "//android.widget.ImageButton[@content-desc='Back']"
    }

    # Click agree btn and ok btn to allow permission
    btn_agree_xpath = locators["btn_agree"]
    driver.find_element("xpath", btn_agree_xpath).click()
    driver.find_element("xpath", btn_agree_xpath).click()
    logging.info("Click btn_agree twice")

    time.sleep(5)

    ok_btn_xpath = locators["ok_btn"]
    driver.find_element("xpath", ok_btn_xpath).click()
    logging.info("Click ok_btn")

    time.sleep(5)

    # Click permission btn of location
    permission_allow_one_time_button_xpath = locators["permission_allow_one_time_button"]
    driver.find_element("xpath", permission_allow_one_time_button_xpath).click()
    logging.info("Click permission_allow_one_time_button ")

    time.sleep(3)

    # Allow app to located always
    allow_always_radio_button_xpath = locators["allow_always_radio_button"]
    driver.find_element("xpath", allow_always_radio_button_xpath).click()
    logging.info("Click allow_always_radio_button ")

    time.sleep(3)

    # Finished above steps and click back btn
    back_page_btn_xpath = locators["back_page_btn"]
    driver.find_element("xpath", back_page_btn_xpath).click()
    logging.info("Click back_page_btn ")

def skip_app_start_page():
    """
    Skip app guide page
    """

    locators = {
        "next_page_btn": "//android.widget.ImageView[@content-desc='Next page']",
        "close_btn": "//android.widget.ImageView[@content-desc='Close']"
    }

    # Click next page to skip guide page
    next_page_btn_xpath = locators["next_page_btn"]
    driver.find_element("xpath", next_page_btn_xpath).click()
    logging.info("Click next_page_btn ")

    time.sleep(3)

    next_page_btn_xpath = locators["next_page_btn"]
    driver.find_element("xpath", next_page_btn_xpath).click()
    logging.info("Click next_page_btn ")

    time.sleep(3)

    close_btn_xpath = locators["close_btn"]
    driver.find_element("xpath", close_btn_xpath).click()
    logging.info("Click close_btn ")

def navigate_to_nine_forecast_page(driver):
    """
    Navigate to 9-Day Forecast page from homepage
    """

    locators = {
        "navigate_up_btn": "//android.widget.ImageButton[contains(@content-desc, 'Navigate up')]",
        "forecast_section_btn": "//android.widget.TextView[@text='Forecast & Warning Services']",
        "nine_forecast_section_btn": "//android.widget.TextView[@resource-id='hko.MyObservatory_v1_0:id/title' and @text='9-Day Forecast']"
    }

    # Click upper left btn to expand directory
    navigate_up_btn_xpath = locators["navigate_up_btn"]
    driver.find_element("xpath", navigate_up_btn_xpath).click()
    logging.info("Click navigate_up_btn ")

    time.sleep(3)

    # Click forecast section bar
    forecast_section_btn_xpath = locators["forecast_section_btn"]
    driver.find_element("xpath", forecast_section_btn_xpath).click()
    logging.info("Click forecast_section_btn ")

    time.sleep(3)

    # Click 9-Day forecast section btn
    nine_forecast_section_btn_xpath = locators["nine_forecast_section_btn"]
    driver.find_element("xpath", nine_forecast_section_btn_xpath).click()
    logging.info("Click nine_forecast_section_btn ")

def screenshot(driver):
    """
    Screenshot and save file
    """

    datetime = time.strftime("%Y-%m-%d_%H:%M:%S")
    directory = '%s/' % os.getcwd()
    file_name = 'screenshot_' + datetime + '.png'

    driver.save_screenshot(directory + file_name)
    logging.info("Save screenshot! ")

def task02():

    # Launch driver and app
    logging.info("Launch driver.")
    initial_driver()

    time.sleep(5)

    skip_initial_app_page(driver)

    time.sleep(5)

    skip_app_start_page()

    time.sleep(5)
    
    navigate_to_nine_forecast_page(driver)
    
    time.sleep(5)
    
    screenshot(driver)

    driver.quit()
    logging.info("Case Done")

if __name__ == "__main__":
    task02()