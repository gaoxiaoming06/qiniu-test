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
    driver.tap([(300, 200)])
    driver.find_element_by_xpath('//*[@text="进入支付宝"]').click()
#     driver.find_element_by_xpath('//*[@text="密码"]').click()
#     driver.find_element_by_xpath('//*[@text="请输入登录密码"]').send_keys("mwj910809")
#     driver.find_element_by_xpath('//*[@text="登录"]').click()

count = int(input("请输入循环次数："))
step = int(input("请输入初始值："))
# countPF = int(input("请输入浦发次数："))
bankSelf = ""
amountSelf = ""
while True:
    checkBank = []

    questions = [
        {
            "type": "list",
            "message": "请选择一张卡片:",
            "choices": ["交通银行信用卡", "广发银行信用卡", "中信银行信用卡", "光大银行信用卡", "上海银行信用卡",
                        "浦发银行信用卡", "平安银行信用卡", "建设银行信用卡", "招商银行信用卡", "工商银行信用卡",
                        "兴业银行信用卡", "南京银行信用卡", "江苏银行信用卡", "农业银行信用卡"],
            "default": None,
        }
    ]

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

    amountList = []

    print("------第 " + str(step) + " 次开始------")

    if step <= 3:
        checkBank.append(questions[0].get("choices")[1])  #广发
        amountList = amountListLarge
    elif step <= 8:
        checkBank.append(questions[0].get("choices")[2])  #中信
        amountList = amountListLarge
    elif step <= 9:
        checkBank.append(questions[0].get("choices")[3])  # 光大
        amountList = amountListLarge
    elif step <= 11:
        checkBank.append(questions[0].get("choices")[13])  # 农业
        amountList = amountListLarge
    elif step <= 14:
        checkBank.append(questions[0].get("choices")[0])  # 交通
        amountList = amountListMicro
    elif step <= 15:
        checkBank.append(questions[0].get("choices")[5])   # 浦发
        amountList = amountListLarge
    elif step <= 16:
        checkBank.append(questions[0].get("choices")[12])   # 江苏
        amountList = amountListLarge
    # elif step <= 14 + countPF:
    #     checkBank.append(questions[0].get("choices")[5])
    #     amountList = amountListMiddle
    else:
        if len(bankSelf) == 0 or len(amountSelf) == 0:
            bankSelf = prompt(questions=questions)[0]  # 自选银行
            amountSelf = prompt(questions=questionsAmount)  # 自选金额
        checkBank.append(bankSelf)
        resultAmount = amountSelf
        if resultAmount[0] == "small":
            amountList = amountListSmall
        elif resultAmount[0] == "middle":
            amountList = amountListMiddle
        elif resultAmount[0] == "large":
            amountList = amountListLarge
        elif resultAmount[0] == "micro":
            amountList = amountListMicro

    print("当前配置: " + str(checkBank) + "  " + str(amountList))

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

    # 信用卡额度用完校验
    viewRes = driver.find_elements_by_class_name("android.widget.TextView")
    checkCredit = bool()
    for res in viewRes:
        if "信用卡" in res.text:
            checkCredit = 1
            break
    if not checkCredit:
        print("信用卡额度用完...")
        break

    # 是否领积分校验
    # viewResIntegral = driver.find_elements_by_class_name("android.widget.TextView")
    # checkIntegral = bool()
    # for resIntegral in viewResIntegral:
    #     if "支付宝积分" in resIntegral.text:
    #         checkIntegral = 1
    #         break
    # if checkIntegral:
    #     driver.tap([(912, 822)])

    time.sleep(6)
    # driver.tap([(driver.get_window_size()['width'] / 2, driver.get_window_size()['height'] - 20)])
    driver.back()
    time.sleep(6)
    driver.back()

    print("------第 " + str(step) + " 次结束------\n")
    step += 1
    count -= 1
    if count == 0:
        break

driver.quit()
