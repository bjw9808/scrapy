import pyautogui
import time
import win32gui, win32ui, win32con, win32api
import hashlib
import os

pyautogui.FAILSAFE = True
global behind_filename
global behind_md5
behind_filename = None
behind_md5 = None

def get_wechat_coordinate():
    x_coordinate = input('输入微信在任务栏的x坐标：')
    y_coordinate = input('输入微信在任务栏的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 1677, 1058

def get_chat_coordinate():
    x_coordinate = input('输入微信聊天的x坐标：')
    y_coordinate = input('输入微信聊天的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 564, 321

def get_first_chat_coordinate():
    x_coordinate = input('输入微信第一行聊天的x坐标：')
    y_coordinate = input('输入微信第一行聊天的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 687, 321

def get_final_chat_coordinate():
    x_coordinate = input('输入微信聊天框右下角的x坐标：')
    y_coordinate = input('输入微信聊天框右下角的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 1384, 813

def get_start_chat_coordinate():
    x_coordinate = input('输入微信聊天框左上角的x坐标：')
    y_coordinate = input('输入微信聊天框左上角的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 536, 226

def clict_once():
    pyautogui.click(clicks=1)

def move_mouse_to_location(x_coordinate, y_coordinate):
    pyautogui.moveTo(int(x_coordinate), int(y_coordinate))

def clict_twice():
    pyautogui.click(clicks=2)

def screenshot(start_x, start_y, finish_x, finish_y, filename):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, finish_x, finish_y)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (finish_x, finish_y), mfcDC, (start_x, start_y), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

def save_behind_filename(filename):
    global behind_filename
    behind_filename = filename
    return behind_filename

def save_behind_hash(filename):
    global behind_md5
    behind_md5 = hash_calculate(filename)
    return

def hash_calculate(filename):
    with open(filename, 'rb') as f:
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_final = md5_obj.hexdigest()
    return str(hash_final).upper()

def del_file(filename):
    os.remove(filename)

if __name__ == '__main__':
    wechat_coordinate = get_wechat_coordinate()
    chat_coordinate = get_chat_coordinate()
    first_chat_coordinate = get_first_chat_coordinate()
    start_chat_coordinate = get_start_chat_coordinate()
    final_chat_coordinate = get_final_chat_coordinate()

    # 我的配置，下次应该改成config文件比较好
    # wechat_coordinate = 1677, 1058
    # chat_coordinate = 564, 321
    # first_chat_coordinate = 687, 321
    # start_chat_coordinate = 536, 226
    # final_chat_coordinate = 1384, 813
    
    while 1:
        if behind_md5 and behind_filename:
            filename = 'screenshot-{}.jpg'.format(int(time.time()))
            move_mouse_to_location(wechat_coordinate[0], wechat_coordinate[1])
            clict_twice()
            move_mouse_to_location(chat_coordinate[0], chat_coordinate[1])
            clict_twice()
            move_mouse_to_location(first_chat_coordinate[0], first_chat_coordinate[1])
            clict_once()
            screenshot(start_chat_coordinate[0],
                       start_chat_coordinate[1],
                       final_chat_coordinate[0] - start_chat_coordinate[0],
                       final_chat_coordinate[1] - start_chat_coordinate[1],
                       filename)
            new_hash = hash_calculate(filename)
            if new_hash == behind_md5:
                del_file(filename)
            else:
                save_behind_filename(filename)
                save_behind_hash(filename)
        else:
            filename = 'screenshot-{}.jpg'.format(int(time.time()))
            move_mouse_to_location(wechat_coordinate[0], wechat_coordinate[1])
            clict_twice()
            move_mouse_to_location(chat_coordinate[0], chat_coordinate[1])
            clict_twice()
            move_mouse_to_location(first_chat_coordinate[0], first_chat_coordinate[1])
            clict_once()
            screenshot(start_chat_coordinate[0],
                       start_chat_coordinate[1],
                       final_chat_coordinate[0] - start_chat_coordinate[0],
                       final_chat_coordinate[1] - start_chat_coordinate[1],
                       filename)
            save_behind_filename(filename)
            save_behind_hash(filename)