import unittest
from appium import webdriver

desired_caps = dict(
    platformName='Android',
    platformVersion='11',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    app='/Users/abc/Workspace/fitbud/fb_app/build/app/outputs/apk/release/app-release.apk'
)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
   
def test_data():
    print('testing...')
    data = driver.current_context
    print(f'data: {data}')

