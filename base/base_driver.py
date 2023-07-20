from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput

def init_driver(no_reset=True):
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["appium:automationName"] = "UiAutomator2"
    desired_caps["appium:deviceName"] = "cfbb7ee1"
    desired_caps["appium:ensureWebviewsHavePages"] = True
    desired_caps["appium:nativeWebScreenshot"] = True
    desired_caps["appium:newCommandTimeout"] = 3600
    desired_caps["appium:connectHardwareKeyboard"] = True
    desired_caps["appium:noReset"] = no_reset
    return webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    # desired_caps = dict()
    # desired_caps['platformVersion'] = '11.0'
    # desired_caps['appPackage'] = 'com.voyah.os.carlauncher'
    # desired_caps['appActivity'] = 'com.voyah.os.carlauncher.second.LauncherActivityMainSecond'

if __name__ == '__main__':
    init_driver()
