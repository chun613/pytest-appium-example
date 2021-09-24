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

3. Run appium  
- Install appium: https://appium.io/docs/en/about-appium/getting-started/?lang=en  
- Export environment variable ANDROID_HOME point to android sdk 
```
# exmaple 
$ export ANDROID_HOME=/Users/abc/Library/Android/sdk
```

4. Start appium
```bash
$ appium
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
```
