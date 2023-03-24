import pyautogui
import pyperclip
import time
import bing
import poe


# 打开微信窗口
pyautogui.hotkey('winleft', '1')

# 等待聊天记录加载完成
time.sleep(1)

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # 设置tesseract路径

def is_wechat_top():
    image_location = pyautogui.locateOnScreen("sousuo.png", confidence=0.8)
    if image_location:
        return True
    else:
        return False


def back_home():
    backbutton = pyautogui.locateOnScreen('back.png', confidence=0.8)
    if backbutton:
        backbutton_pos = pyautogui.center(backbutton)
        pyautogui.click(backbutton_pos)
    else:
        pyautogui.hotkey('winleft', '1')
        time.sleep(1)

def reply_msg(user):
    print(f"开始回复【{user}】")

# def get_user_name(pos):
#     at_msg_left, at_msg_top = pos
#     screenshot = pyautogui.screenshot(region=(at_msg_left-10, at_msg_top-30, 100, 22))
#     sender_name = pytesseract.image_to_string(screenshot).strip()
#     print("发送人的名称为：", sender_name)

def send_msg(msg):
    input_wind = pyautogui.locateOnScreen('input.png', confidence=0.8)
    input_wind_pos = pyautogui.center(input_wind)
    pyautogui.click(input_wind_pos[0]+20, input_wind_pos[1]+20)
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('enter')

# 获取聊天记录
while True:
    chat_records = pyautogui.locateOnScreen('at_me.png', confidence=0.8)
    if chat_records:
        print("找到待处理信息...")
        chat_records_pos = pyautogui.center(chat_records)
        pyautogui.click(chat_records_pos)
        time.sleep(1)
        print("开始寻找@我的具体信息")
        at_msg = list(pyautogui.locateAllOnScreen('at_lgc.png', confidence=0.8))
        if at_msg:
            at_msg_pos = pyautogui.center(at_msg[-1])
            pyautogui.doubleClick(at_msg_pos)
            pyautogui.hotkey('ctrl', 'c')
            chat_records = pyperclip.paste()[5:]
            send_msg(f'好的，关于："{chat_records}"的消息我已经收到！')
            print("已获取提问，等待结果获取")
            answer = poe.reply(chat_records)
            pyautogui.hotkey('winleft', '1')
            send_msg(answer)
            back_home()
            print(chat_records)
            with open('chat_records.txt', 'a', encoding='utf-8') as f:
                f.write(chat_records + '\n')
                print("获得并保存了一个新的聊天信息到到文件。")
        else:
            back_home()
    else:
        print("暂未获得待处理信息")
        if pyautogui.locateOnScreen('wenjian.png', confidence=0.8):
            time.sleep(2)
        else:
            back_home()
