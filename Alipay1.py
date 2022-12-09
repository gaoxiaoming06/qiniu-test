import random
import time

from InquirerPy import prompt
from appium import webdriver

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本
    'udid': '63d04786',  # 设备名，安卓手机可以随意填写
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

if driver.is_locked():
    driver.press_keycode(82)
    # print(driver.page_source)
    driver.find_element_by_xpath('//*[@class="android.widget.EditText"]').send_keys("gjh170507")
    driver.press_keycode(66)

if driver.current_activity == "com.ali.user.mobile.loginupgrade.activity.LoginActivity":
    driver.find_element_by_xpath('//*[@text="进入支付宝"]').click()
#     driver.find_element_by_xpath('//*[@text="密码"]').click()
#     driver.find_element_by_xpath('//*[@text="请输入登录密码"]').send_keys("mwj910809")
#     driver.find_element_by_xpath('//*[@text="登录"]').click()

while True:
    checkBank = []

    number = int(input("请输入循环次数："))
    questions = [
        {
            "type": "list",
            "message": "请选择一张卡片:",
            "choices": ["交通银行信用卡", "广发银行信用卡", "中信银行信用卡", "光大银行信用卡", "上海银行信用卡",
                        "浦发银行信用卡", "平安银行信用卡", "建设银行信用卡", "招商银行信用卡", "工商银行信用卡", "兴业银行信用卡"],
            "default": None,
        }
    ]
    result = prompt(questions=questions)
    checkBank.append(result[0])

    amountListMicro = [6, 7, 8, 9]
    amountListSmall = [12, 13, 14, 15, 16]
    amountListMiddle = [17, 18, 19, 20, 21]
    amountListLarge = [20, 21, 23, 24]
    questionsAmount = [
        {
            "type": "list",
            "message": "请选择金额类型:",
            "choices": ["large", "middle", "small", "micro"],
            "default": None,
        }
    ]
    resultAmount = prompt(questions=questionsAmount)
    amountList = []
    if resultAmount[0] == "small":
        amountList = amountListSmall
    elif resultAmount[0] == "middle":
        amountList = amountListMiddle
    elif resultAmount[0] == "large":
        amountList = amountListLarge
    elif resultAmount[0] == "micro":
        amountList = amountListMicro

    for i in range(number):

        print("第几个了: " + str(i) + "  " + str(checkBank))

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
        driver.swipe(500, 800, 500, 100, 200)
        driver.swipe(500, 800, 500, 100, 200)
        driver.swipe(500, 800, 500, 100, 200)
        driver.swipe(500, 800, 500, 100, 200)
        driver.find_element_by_xpath(
            '//android.widget.ImageView[contains(@content-desc, "2021年02月16日 16点03分")]').click()
        driver.find_element_by_xpath('//*[@text="确定"]').click()
        time.sleep(5)
        amount = amountList[random.randint(0, len(amountList) - 1)]
        print("付款金额: " + str(amount))
        for every_char in str(amount):
            driver.find_element_by_xpath('//*[@text="' + every_char + '"]').click()
            time.sleep(3)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@text="查看全部"]').click()
        time.sleep(3)
        findBank = bool()
        while not findBank:
            viewAll1 = driver.find_elements_by_class_name("android.widget.TextView")
            for view1 in viewAll1:
                if view1.text == checkBank[0]:
                    view1.click()
                    findBank = 1
                    break
            driver.swipe(500, 800, 500, 600, 200)

        driver.find_element_by_xpath('//*[@text="确认付款"]').click()
        time.sleep(2)
        if "使用刷脸" in driver.page_source:
            driver.find_element_by_xpath('//*[@text="使用刷脸"]').click()
            time.sleep(2)
            driver.back()
            driver.find_element_by_xpath('//*[@text="输入密码"]').click()
        if "使用指纹" in driver.page_source:
            if not ("请输入支付密码" in driver.page_source):
                driver.find_element_by_xpath('//*[@text="使用指纹"]').click()
        if "使用密码" in driver.page_source:
            driver.find_element_by_xpath('//*[@text="使用密码"]').click()

        time.sleep(2)
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
    #     time.sleep(6)
    #     driver.back()

driver.quit()
