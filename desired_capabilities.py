def get_desired_capabilities():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",
        "udid": "emulator-5554",
        "app": "/Users/sandy/Desktop/python-appium/bin/thebump_qa.apk",
        "automationName": "Appium",
        "deviceName": "Pixel 2",
        "newCommandTimeout": 20000,
        "appWaitActivity": "com.xogrp.thebump.ui.MainActivity",
        "autoGrantPermissions": True,
        "noReset": True,
        "clearSystemFiles":True
    }
    return desired_caps

def get_uri():
    return 'http://localhost:4723/wd/hub'