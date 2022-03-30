import time

from appium import webdriver

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

# 根据id定位搜索位置框，点击
time.sleep(5)
driver.find_element_by_id("com.alipay.android.widget.fortunehome:id/tab_description").click()
time.sleep(2)
driver.find_element_by_id("com.alipay.android.widget.fortunehome:id/tab_description").click()
time.sleep(2)
driver.find_element_by_id("com.alipay.android.widget.fortunehome:id/tab_description").click()
time.sleep(2)
# driver.find_element_by_xpath(
#     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout").click()
driver.find_element_by_xpath('//*[@text="基金"]').click()
time.sleep(2)

try:
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View[39]/android.widget.Button[2]").click()
except:
    driver.tap([(driver.get_window_size()['width'] / 2, driver.get_window_size()['height'] - 10)])
time.sleep(2)
setData = set([])

allAmount = float()
allLoss = float()
index = int()

viewAll1 = driver.find_elements_by_xpath('//*[contains(@text, "涨跌幅:")]')
for view1 in viewAll1:
    # 打印
    if "估值" in view1.text and "涨跌幅:" in view1.text:
        str111 = ("" + view1.text).replace("%", "").split("涨跌幅:")[1]
        positive = str111[1:2]
        number = str111[2:6]
        ppp = float(number)
        print("percent: " + view1.text)
        setData.add(view1.text)
        index += 1
        if index > 3:
            driver.swipe(100, 800, 100, 600)
        view1.click()
        time.sleep(2)
        try:
            amount = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]")
            print("amount: " + amount.text)
            mmm = float(str(amount.text).replace(",", ""))
            allAmount += mmm
            loss = mmm * ppp / 100
            if positive == "-":
                allLoss -= loss
            else:
                allLoss += loss
            print("当前金额: " + str(mmm) + "  亏损: " + str(loss))
        except:
            driver.back()
            continue
        driver.back()

time.sleep(2)
viewAll2 = driver.find_elements_by_xpath('//*[contains(@text, "涨跌幅:")]')
for view1111 in viewAll2:
    # 打印
    if "估值" in view1111.text and "涨跌幅:" in view1111.text:
        if view1111.text in setData:
            continue
        print("percent: " + view1111.text)
        str111 = ("" + view1111.text).replace("%", "").split("涨跌幅:")[1]
        positive = str111[1:2]
        number = str111[2:6]
        ppp = float(number)
        setData.add(view1111.text)
        driver.swipe(100, 800, 100, 550)
        view1111.click()
        time.sleep(2)
        try:
            amount = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]")
            print("amount: " + amount.text)
            mmm = float(str(amount.text).replace(",", ""))
            allAmount += mmm
            loss = mmm * ppp / 100
            if positive == "-":
                allLoss -= loss
            else:
                allLoss += loss
            print("当前金额: " + str(mmm) + "  亏损: " + str(loss))
        except:
            driver.back()
            continue
        driver.back()

time.sleep(2)
viewAll2 = driver.find_elements_by_xpath('//*[contains(@text, "涨跌幅:")]')
for view1111 in viewAll2:
    # 打印
    if "估值" in view1111.text and "涨跌幅:" in view1111.text:
        if view1111.text in setData:
            continue
        print("percent: " + view1111.text)
        str111 = ("" + view1111.text).replace("%", "").split("涨跌幅:")[1]
        positive = str111[1:2]
        number = str111[2:6]
        ppp = float(number)
        setData.add(view1111.text)
        driver.swipe(100, 800, 100, 550)
        view1111.click()
        time.sleep(2)
        try:
            amount = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]")
            print("amount: " + amount.text)
            mmm = float(str(amount.text).replace(",", ""))
            allAmount += mmm
            loss = mmm * ppp / 100
            if positive == "-":
                allLoss -= loss
            else:
                allLoss += loss
            print("当前金额: " + str(mmm) + "  亏损: " + str(loss))
        except:
            driver.back()
            continue
        driver.back()

time.sleep(2)
viewAll2 = driver.find_elements_by_xpath('//*[contains(@text, "涨跌幅:")]')
for view1111 in viewAll2:
    # 打印
    if "估值" in view1111.text and "涨跌幅:" in view1111.text:
        if view1111.text in setData:
            continue
        print("percent: " + view1111.text)
        str111 = ("" + view1111.text).replace("%", "").split("涨跌幅:")[1]
        positive = str111[1:2]
        number = str111[2:6]
        ppp = float(number)
        setData.add(view1111.text)
        driver.swipe(100, 800, 100, 550)
        view1111.click()
        time.sleep(2)
        try:
            amount = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]")
            print("amount: " + amount.text)
            mmm = float(str(amount.text).replace(",", ""))
            allAmount += mmm
            loss = mmm * ppp / 100
            if positive == "-":
                allLoss -= loss
            else:
                allLoss += loss
            print("当前金额: " + str(mmm) + "  亏损: " + str(loss))
        except:
            driver.back()
            continue
        driver.back()

print("总金额: " + str(allAmount) + "  总亏损: " + str(allLoss) + "  收益率: " + str(allLoss / allAmount * 100) + "%")

# input('**** Press to quit..')
driver.quit()
