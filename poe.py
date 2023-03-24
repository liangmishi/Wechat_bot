import pyautogui
import pyperclip
import time

def reply(qus):
    pyautogui.hotkey('winleft', '2')
    time.sleep(1)
    send_msg(qus)
    answer = copy_answer()
    if answer:
        return answer
    else:
        return False


def send_msg(msg):
    while True:
        input_wind = pyautogui.locateOnScreen('poe_input.png', confidence=0.8)
        if input_wind:
            input_wind_pos = pyautogui.center(input_wind)
            pyautogui.click(input_wind_pos[0]+50, input_wind_pos[1])
            pyperclip.copy(msg)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.hotkey('enter')
            while True:
                time.sleep(1)
                send_wind = pyautogui.locateOnScreen('poe_sending.png', confidence=0.8)
                if not send_wind:
                    failed_wind = pyautogui.locateOnScreen('poe_failed.png', confidence=0.8)
                    if not failed_wind:
                        print('发送成功')
                        pyautogui.moveTo(input_wind_pos[0]+50, input_wind_pos[1]-100)
                        break
                    else:
                        print('发送失败，重新发送')
                        pyautogui.hotkey('F5')
                        time.sleep(2)
                        pyautogui.click(input_wind_pos)
                        send_msg(msg)
                else:
                    print('正在发送')
            break
        else:
            print('未找到输入栏,等待加载')
            pyautogui.hotkey('F5')
            time.sleep(2)

def answer_done():
    while True:
        pyautogui.scroll(-100)
        done_wind = pyautogui.locateOnScreen('poe_done.png', confidence=0.8)
        if done_wind:
            print('回答完毕')
            return True
        else:
            time.sleep(1)
            print('仍在回答')

def copy_answer():
    if answer_done():
        while True:
            done_wind = pyautogui.locateOnScreen('poe_done.png', confidence=0.8)
            answer_pos = pyautogui.center(done_wind)
            pyautogui.click(answer_pos[0]+50, answer_pos[1]-50, button='right')
            time.sleep(1)
            copy_wind = pyautogui.locateOnScreen('poe_copy.png', confidence=0.8)
            if copy_wind:
                copy_pos = pyautogui.center(copy_wind)
                pyautogui.click(copy_pos)
                copy_msg = pyperclip.paste()
                return copy_msg
            else:
                time.sleep(1)
    else:
        print('获取失败')
        return False
