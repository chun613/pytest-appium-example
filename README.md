# pytest-appium-example

## Usage

1. Setup virtual environment
```bash
$ python3 -m venv venv 
$ source ./venv/bin/activate
```

2. Install library
```bash
(venv) $ python3 -m pip install -r requirements.txt
```  

3. Install appium  
Install appium: https://appium.io/docs/en/about-appium/getting-started/?lang=en  

```
# Exmaple for mac
$ brew install appium
...
```

4. Run appium with variable, in separate terminal  
Export environment variable ANDROID_HOME point to android sdk 
```bash
$ export ANDROID_HOME=/Users/abc/Library/Android/sdk
$ appium
...
```

5. Change unit test parameters  
platformName='Android',  
platformVersion='11' // android os version  
automationName='uiautomator2',  
deviceName='Android Emulator',  
app='/Users/abc/workspace/abc.apk' // apk location

6. Run test
```bash
$ pytest main.py -s

================================================ test session starts =================================================
platform darwin -- Python 3.7.12, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/abc/Workspace/pytest-appium-example
collected 1 item

main.py testing...
data: NATIVE_APP
.

================================================= 1 passed in 12.42s =================================================
(venv) ➜  pytest-appium-example git:(main) ✗
```
