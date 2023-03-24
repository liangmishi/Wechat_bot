import pyautogui
import pyperclip
import time

def reply(qus):
    pyautogui.hotkey('winleft', '2')
    time.sleep(1)
    send_msg(qus)
    answer = copy_answer()
    if answer == '很抱歉，我认为我们需要继续！让我们切换到 newtopic 并重新开始。':
        send_msg(qus)
        answer = copy_answer()
    else:
        return answer


def send_msg(msg):
    input_wind = pyautogui.locateOnScreen('bing_input.png', confidence=0.8)
    input_wind_pos = pyautogui.center(input_wind)
    pyautogui.click(input_wind_pos)
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    while True:
        wait_wind = pyautogui.locateOnScreen('waiting.png', confidence=0.8)
        if wait_wind:
            print('开始响应')
            break
        else:
            time.sleep(1)
            print('等待响应')

# send_msg('你好')

def answer_done():
    while True:
        if pyautogui.locateOnScreen('waiting.png', confidence=0.8):
            print('仍在响应')
            time.sleep(1)
        else:
            time.sleep(3)
            print('确认响应是否完成')
            if pyautogui.locateOnScreen('waiting.png', confidence=0.8):
                time.sleep(1)
            else:
                time.sleep(5)
                print('再次确认响应是否完成')
                if pyautogui.locateOnScreen('waiting.png', confidence=0.8):
                    time.sleep(1)
                else:
                    print('回答完毕')
                    return True

def copy_answer():
    if answer_done():
        answer_wind = list(pyautogui.locateAllOnScreen('bing.png', confidence=0.8))
        answer_pos = pyautogui.center(answer_wind[-1])
        pyautogui.click(answer_pos[0]+50, answer_pos[1]+20, button='right')
        time.sleep(1)
        copy_wind = pyautogui.locateOnScreen('copy.png', confidence=0.8)
        copy_pos = pyautogui.center(copy_wind)
        pyautogui.click(copy_pos)
        copy_msg = pyperclip.paste()
        return copy_msg
    else:
        print('获取失败')


