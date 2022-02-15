import time

from appium import webdriver

# 测试之前环境检测
from base.environment import EnvironmentAndroid

# if __name__ == '__main__':
#     env = EnvironmentAndroid()
#     env.check_environment()

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
driver.find_element_by_android_uiautomator('new UiSelector().text("理财").className("android.widget.TextView")').click()
time.sleep(2)
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout").click()
time.sleep(2)
try:
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View[27]/android.widget.Button[2]").click()
except:
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.bc/android.webkit.WebView/android.view.View/android.view.View[28]/android.widget.Button[2]").click()

driver.find_element_by_android_uiautomator('new UiSelector().textContains("自选")').click()



input('**** Press to quit..')
driver.quit()
