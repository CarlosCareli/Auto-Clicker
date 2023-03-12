import pyautogui as pg
import time
from pynput import keyboard

def stop_loop(key):
    if key == keyboard.Key.esc:
        return False  

time.sleep(5)

with keyboard.Listener(on_press=stop_loop) as listener:

    while True:
        
        num_clicks = 20
        for i in range(num_clicks):
            pg.click()
            time.sleep(100) 
            
            if not listener.running:
                break  

        if not listener.running:
            break
