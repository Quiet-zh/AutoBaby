# autobaby/core.py
import schedule
import time
import pyautogui

def auto_click():
    pyautogui.click(x=1000, y=500)  # 示例点击坐标

def start_scheduler():
    schedule.every(10).seconds.do(auto_click) #type: ignore
    while True:
        schedule.run_pending()
        time.sleep(1)
