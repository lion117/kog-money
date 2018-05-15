# -*- coding: utf-8 -*-

import pyautogui
import time

pyautogui.FAILSAFE = False
screenshot = pyautogui.screenshot

pngLocate = pyautogui.locateOnScreen

def click(x,y):
    pyautogui.moveTo(x,y)
    
    pyautogui.click()

def get_button_center_from_screen(button_png,png_path='pics'):
    screen = screenshot("screen.png")
    button_png = png_path + '\\' + button_png
    start_pos = pngLocate(button_png)

    if start_pos == None:
        #找不到button
        print("{} not exsit on current screen".format(button_png))
        return 0,0

    return pyautogui.center(start_pos)

def AutoMouse():
    
    print("Start")

    n = 1

    while(n<60):
        
        print("{now} 第{n}次\n".format(now=time.strftime("%m-%d %H:%M:%S"), n=n))
        
        x, y = get_button_center_from_screen('开始闯关.PNG')
        click(x,y)
        time.sleep(5)
        
        loading = False
        #是否正在加载中
        while(1):
            x,y = get_button_center_from_screen('加载中.PNG')
            time.sleep(3)
            if (x,y) != (0,0):
                break
        
        loading = False
        print("加载中\n")
        
        while(1):
            x,y = get_button_center_from_screen('加载中.PNG')
            if (x,y) == (0,0):
                break
        
        print("加载完成\n")
        

        #检查是否初始画面需要跳过
        x,y = get_button_center_from_screen('跳过.PNG')
        if (x,y) == (0,0):
            print("no need Jump over")
        else:
            print("need Jump over")
            click(x,y)
            
        #检查是否已经启用自动
        x,y = get_button_center_from_screen("未启用自动.PNG")
        if (x,y) != (0,0):
            print("not auto run")
            click(x,y)
        else:
            print("already auto run")
            
            
        #运行监测，是否结束，以及中间存在需要跳过，结束则开启下一次  每5s检测一次
        while(1):
            time.sleep(3)
            x,y = get_button_center_from_screen('跳过2.PNG')
            if (x,y) == (0,0):
                print("no need Jump over")
            else:
                print("need Jump over")
                click(x,y)
            
            x,y = get_button_center_from_screen("结束后继续.PNG")
            if (x,y) == (0,0):
                print("not over")
            else:
                print("all over.\n")
                click(x,y)
                time.sleep(5)
                
                #start 闯关
                print("Start again")
                x, y = get_button_center_from_screen('再次挑战.PNG')
                n = n+1
                click(x,y)
                time.sleep(10)
                break

if __name__ == '__main__':
    AutoMouse()

