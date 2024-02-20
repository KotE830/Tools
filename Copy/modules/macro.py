import keyboard
import pyautogui
import pyperclip

from configs import config

def get_mouse_position():
  keyboard.wait(config.setting_key)
  return tuple(pyautogui.position())

def click(pos):
  pyautogui.click(pos)

def drag(start, end):
  pyautogui.moveTo(*start)
  pyautogui.mouseDown()
  pyautogui.moveTo(end)
  # pyautogui.dragTo(*end, 0.2)
  pyautogui.mouseUp()

def copy():
  pyautogui.hotkey(config.copy_key)
  return pyperclip.paste()

def paste_in_excel(sheet, words):
  if words == []:
    return
  
  if words[-1][-1] == ",":
    words[-1] = words[-1][:-1]
  
  word = [words[0], words[1], " ".join(words[2:])]

  sheet.append(word)

  # c2 = sheet.cell(row=1, column=2)
  # c2.value = "98"

  # c3 = sheet["A2"]
  # c3.value = "roqudtls"

def wait_end():
  keyboard.wait(config.end_key)