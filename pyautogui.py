import pyautogui

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

#button_x, button_y = pyautogui.locateCenterOnScreen('create_button.png')
#pyautogui.click(button_x, button_y)

# Get the current mouse position
currentMouseX, currentMouseY = pyautogui.position()

# mouse movement
pyautogui.moveTo(100,100,duration=2)
pyautogui.moveRel(200,0,duration=2)

# click
pyautogui.click(100,100)
pyautogui.doubleClick(100,100)
pyautogui.rightClick(100,100)

# drag
pyautogui.dragTo(100,100,duration=2)
pyautogui.dragRel(200,0,duration=2)

# scroll
pyautogui.scroll(200)

# keyboard
pyautogui.write('hello world', interval=0.25)
pyautogui.typewrite('Hello world!')
pyautogui.press('enter')
pyautogui.press('tab', presses=3)
pyautogui.press(['a', 'b', 'c'])
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')

# Press the key combination "Ctrl+C"
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl','o').typewrite('Hello world!', interval=0.25)

# screenshot
im1 = pyautogui.screenshot()
im1.save('im1.png')

# locate
picLoc = pyautogui.locateOnScreen('im2.png', confidence=0.9) # pip install opencv-python
picLoc = pyautogui.locateCenterOnScreen('im2.png')
pyautogui.moveTo(picLoc, duration=2)

# prompts
myText = pyautogui.prompt(text="hello world", title="myPrompBox")
myConfirm = pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])

# pause timeout
pyautogui.PAUSE = 2.5

# Common Key Values
Alphanumeric: 'a', 'b', 'c', '1', '2', '3', etc.
Function Keys: 'f1', 'f2', 'f3' ... up to 'f12'
Navigation: 'left', 'right', 'up', 'down', 'home', 'end', 'pageup', 'pagedown'
Editing: 'enter', 'backspace', 'tab', 'space', 'delete', 'insert'
Modifiers: 'shift', 'ctrl', 'alt', 'command', 'option', 'win' (Windows key)
System: 'esc', 'printscreen', 'scrolllock', 'pause', 'capslock', 'numlock'
