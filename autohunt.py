import pyautogui
import time

#from selenium import webdriver

def open_discord():
    pyautogui.hotkey('alt', 'tab')
    return


def hunt_battle():
    pyautogui.typewrite('owoh\n', interval=0.2)
    time.sleep(1)
    pyautogui.typewrite('owob\n', interval=0.2)
    time.sleep(1)
    #pyautogui.typewrite('owosell all\n')
    pyautogui.typewrite('owo\n', interval=0.2)
    time.sleep(20)

def main():
    print('Started script...')
    open_discord()
    #time.sleep(5)
    n = 0
    while True:
        hunt_battle()
        n += 1
        print(n, 'cycle(s) completed')
        

if __name__ == '__main__':
    main()
