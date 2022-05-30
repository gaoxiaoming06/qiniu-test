import os
import time

import psutil as psutil
import pyautogui as pyautogui
import pyperclip as pyperclip
import urllib3
import win32api
import win32con
import win32gui
from bs4 import BeautifulSoup

http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
response = http.request('GET', 'https://github.com/freefq/free', timeout=5.0, retries=100)  # get方式请求
soup = BeautifulSoup(response.data.decode('utf-8'),"html.parser")
delegate = str()
for i in soup.find_all('pre', attrs={"pre":""}):
    delegate = delegate.join(str(i))
pyperclip.copy(delegate)
print(delegate)
app_dir = r'D:\Program Files\v2rayN-Core\v2rayN.exe'
hasStart = bool()
pl = psutil.pids()
for pid in pl:
    if psutil.Process(pid).name() == 'v2rayN.exe':
        hasStart = 1
        break
if not hasStart:
    os.startfile(app_dir)
time.sleep(5)
pyautogui.click(1660, 1385, button='left')
# pyautogui.click(800, 500, button='left')
# win32api.keybd_event(17, 0, 0, 0)
# win32api.keybd_event(65, 0, 0, 0)
# win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(46, 0, 0, 0)
# win32api.keybd_event(46, 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(13, 0, 0, 0)
# win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(17, 0, 0, 0)
# win32api.keybd_event(86, 0, 0, 0)
# win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(13, 0, 0, 0)
# win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

# TODO 操作窗口到前台
# def windowEnumerationHandler(hwnd, top_windows):
#     top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
# top_windows = []
# win32gui.EnumWindows(windowEnumerationHandler, top_windows)
# for i in top_windows:
#     print(i)
#     if "v2rayN" in i[1]:
#         print(i)
#         win32gui.ShowWindow(i[0], 5)
#         win32gui.SetForegroundWindow(i[0])
