from appium import webdriver
import time

appium_connect={}
appium_connect['deviceName']='ba8749b7'
appium_connect['platformName']='Andriod'
appium_connect['platformVersion']='6.0.1'
appium_connect['appPackage']='com.xingin.xhs'
appium_connect['appActivity']='.index.v2.IndexActivityV2'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',appium_connect)
time.sleep(5)
print(driver)