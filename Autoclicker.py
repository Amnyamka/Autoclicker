from tkinter import *
import tkinter as tk
import time
import threading
import sys
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode



HEIGHT = 150
WIDTH = 300


root = tk.Tk()
delay = 1.000
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):

    def __init__(self, delay, button):
        threading.Thread.__init__(self)
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        root.protocol('WM_DELETE_WINDOW', self.exit)
        print('init checked')

    def start_clicking(self):
        self.running = True
        print('start checked')

    def stop_clicking(self):
        self.running = False
        print('stop checked')

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        print('exit checked')
        sys.exit()

    def run(self):
        print('run checked')
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)




class Application(ClickMouse):


    def interface(self):

        self.canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        self.frame = tk.Frame(root, bg='#80c1ff')
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.entry = tk.Entry(self.frame, text='')
        self.entry.place(relx=0.3, rely=0.25, relwidth=0.1, relheight=0.15)
        self.sec = self.entry.get()

        self.button = tk.Button(self.frame, text="Change speed", command=self.changedelay)
        self.button.place(relx=0.5, rely=0.25, relwidth=0.38, relheight=0.15)
        button2 = tk.Button(self.frame, text="Launch", command=self.launch)
        button2.place(relx=0.5, rely=0.77, relwidth=0.38, relheight=0.15)

        label = tk.Label(self.frame, text="Autoclicker v0.2 by Amnyam", bg='#80c1ff')
        label.place(relx=0.22, rely=0)
        label2 = tk.Label(self.frame, text="Clicks per sec:", bg='#80c1ff')
        label2.place(relx=0, rely=0.25)
        label3 = tk.Label(self.frame, text="S - start/stop, E - exit", bg='#80c1ff')
        label3.place(relx=0, rely=0.77)

        root.mainloop()

    def launch(self):
        self.button = button
        click_thread.start()
        root.destroy()
        print(self.delay)

    def changedelay(self):
        self.delay = (float(1.0) / float(int(self.entry.get())))
        print(self.delay)



mouse = Controller()
click_thread = Application(delay, button)
click_thread.interface()

def on_press(key):
    print('on_press checked')
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()