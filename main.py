import unittest
# from pathlib import Path
# import os
from appium import webdriver


desired_caps = dict(
    platformName='Android',
    platformVersion='11',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    app='/Users/chengkachun/Workspace/fitbud/fb_app/build/app/outputs/apk/release/app-release.apk'
)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


   
def test_data():
    print('testing...')
    data = driver.current_context

    # data = driver.get_performance_data('com.example.fb_app.MainActivity', 'cpuinfo', 5)
    print(f'data: {data}')

