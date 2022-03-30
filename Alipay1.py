import time

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.eg.android.AlipayGphone',  # 启动APP Package名称
    'appActivity': '.AlipayLogin',  # 启动Activity名称
    'unicodeKeyboard': False,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': False,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
    # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# , "兴业银行信用卡"
# , "招商银行信用卡"
checkBank = ["广发银行信用卡", "交通银行信用卡", "平安银行信用卡", "工商银行信用卡"]

money = int()

time.sleep(10)
n = 18
for i in range(n):
    if i == 5:
        checkBank.pop(0)
    if i == 8:
        checkBank.pop(0)
    if i == n - 2:
        checkBank.pop(0)
    # if i <= 9:
    #     continue

    driver.tap([(990, 130)])
    driver.find_element_by_xpath('//*[@text="扫一扫"]').click()
    time.sleep(2)
    driver.find_element_by_id("com.alipay.mobile.scan:id/title_bar_album").click()
    time.sleep(2)
    driver.swipe(500, 800, 500, 100, 200)
    driver.swipe(500, 800, 500, 100, 200)
    driver.swipe(500, 800, 500, 100, 200)
    driver.swipe(500, 800, 500, 100, 200)
    driver.swipe(500, 800, 500, 100, 200)
    driver.swipe(500, 800, 500, 100, 200)
    driver.find_element_by_xpath('//android.widget.ImageView[contains(@content-desc, "2021年02月16日 16点03分")]').click()
    driver.find_element_by_xpath('//*[@text="确定"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@text="2"]').click()
    time.sleep(3)
    if i == n - 1:
        driver.tap([(driver.get_window_size()['width'] - 15, 1600)])
        remaining = 500 - money
        for every_char in str(remaining):
            driver.find_element_by_xpath('//*[@text="' + every_char + '"]').click()
            time.sleep(3)
    # elif i == n - 1:
    #     driver.tap([(driver.get_window_size()['width'] - 15, 1600)])
    #     remaining1 = 123
    #     for every_char1 in str(remaining1):
    #         driver.find_element_by_xpath('//*[@text="' + every_char1 + '"]').click()
    #         time.sleep(3)
    else:
        if i % 4 == 0:
            driver.find_element_by_xpath('//*[@text="3"]').click()
            money += 23
        if i % 4 == 1:
            driver.find_element_by_xpath('//*[@text="5"]').click()
            money += 25
        if i % 4 == 2:
            driver.find_element_by_xpath('//*[@text="1"]').click()
            money += 21
        if i % 4 == 3:
            driver.find_element_by_xpath('//*[@text="4"]').click()
            money += 24
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]").click()
    time.sleep(3)
    driver.swipe(500, 800, 500, 600, 200)
    viewAll1 = driver.find_elements_by_class_name("android.widget.TextView")
    for view1 in viewAll1:
        if view1.text == checkBank[0]:
            view1.click()
            break

    driver.find_element_by_xpath('//*[@text="使用密码"]').click()
    driver.tap([(driver.get_window_size()['width'] / 2, driver.get_window_size()['height'] - 6)])
    driver.tap([(10, 1600)])
    driver.tap([(driver.get_window_size()['width'] / 2, 1600)])
    driver.tap([(10, 1680)])
    driver.tap([(driver.get_window_size()['width'] / 2, 1680)])
    driver.tap([(10, 1680)])

    time.sleep(6)
    driver.tap([(500, 700)])
    time.sleep(6)
    # driver.tap([(driver.get_window_size()['width'] / 2, driver.get_window_size()['height'] - 20)])
    driver.back()
    time.sleep(6)
    driver.back()

driver.quit()
