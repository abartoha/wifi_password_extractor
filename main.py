"""
Application Functionality: Extracts wifi passwords and shows them on a
Tcl/tk GUI

This tool can be used to extract passwords from a laptop or
computer that is connected with a wifi with a password to
just squeeze a password out of it, it is very practical for 
suddent usages, and will benefit a lot of people, and also hurt
others so do it at your own risk and concern, this isn't my fault!

Afterword:
I am very proud of this one because this is one of my first OOP GUI and
OOP codes, much organised
"""
#Variables
GEOMETRY = "400x300"

from tkinter import *
from tkinter import messagebox
import subprocess
from base64 import b64decode
from os import remove

#ICON
#Steps to embedding icons into a py file
#   1. base64 the icon (by manual or from an online tool which I did :p) and add it in here as a string
#   2. decode it here inside and write a temporary file at runtime, also you can remove it after it's been used during runtime
icon = "AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAHwdAAB8HQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBAAAAQQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABKAAAA4QAAAOEAAABKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAApgAAAPsAAAD7AAAApgAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAArAAAAFAAAABIAAABEAAAARAAAABIAAAAUAAAALAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABKAAAA3AAAALoAAABUAAAAJgAAACYAAABUAAAAugAAANwAAABKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOAAAAtAAAAP8AAAD/AAAA+gAAAOoAAADqAAAA+gAAAP8AAAD/AAAAtAAAAA4AAAAAAAAAAAAAAAEAAAA2AAAAIwAAACcAAACgAAAA7QAAAP8AAAD/AAAA/wAAAP8AAADtAAAAoAAAACcAAAAjAAAANgAAAAEAAABUAAAA3gAAAMwAAABHAAAACwAAADAAAABpAAAAigAAAIoAAABpAAAAMAAAAAsAAABHAAAAzAAAAN4AAABUAAAAsAAAAP4AAAD/AAAA8AAAAKkAAABXAAAAKQAAABkAAAAZAAAAKQAAAFcAAACpAAAA8AAAAP8AAAD+AAAAsAAAABsAAACQAAAA8QAAAP8AAAD/AAAA+wAAAOsAAADdAAAA3QAAAOsAAAD7AAAA/wAAAP8AAADxAAAAkAAAABsAAAAAAAAABgAAAEcAAACtAAAA6gAAAP4AAAD/AAAA/wAAAP8AAAD/AAAA/gAAAOoAAACtAAAARwAAAAYAAAAAAAAAAAAAAAAAAAAAAAAACAAAAC8AAABjAAAAiwAAAJ8AAACfAAAAiwAAAGMAAAAvAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AAD+fwAA/D8AAPgfAADgBwAA4AcAAMADAAAAAAAAAAAAAAAAAAAAAAAAgAEAAOAHAAD//wAA//8AAA=="
icondata = b64decode(icon)
tempFile = "icon.ico"
with open(tempFile, 'wb') as iconfile:
    iconfile.write(icondata)

class GUI:
    """
    This class handles the whole GUI hooligans
    """
    def __init__(self):
        self.buttons = []
        self.entries = []
        self.texts = []
        self.frames = []
        self.states = []
        pass
    def Text_View(self, text:str,rows, cols):
        self.texts.append(Text(self.app))
        self.texts[-1].insert(1.0,text)
        self.texts[-1].grid(row = rows, column = cols)
        pass
    def run_gui(self):
        self.app = Tk()
        self.app.wm_iconbitmap(tempFile)
        remove('icon.ico')
        self.app.title("WiFi Password Extractor")
        self.app.resizable(False, False)
        self.app.geometry(GEOMETRY)
        return 0
    def mainloop(self):
        self.app.mainloop()
        return 0

class Process:
    """
        This class contains the main processes
        of fetching all the passwords from the 
        system
    """
    def __init__(self):
        self.result = []
        self.profiles = []
        self.data = []
        self.wifis = []
        self.show = ""
        pass
    def run_process(self):
        self.data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        self.wifis = [b.split(":")[1][1:-1] for b in self.data if "All User Profile" in b]
        self.profiles = [i.split(":")[1][1:-1] for i in self.data if "All User Profile" in i]
        for i in self.profiles:
            self.result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        self.result = [b.split(":")[1][1:-1] for b in self.result if "Key Content" in b]
        if self.result == []:
            return "No Wifi Passwords Found"
        for i in self.result:
            self.show += f"{self.wifis[self.result.index(i)]}:{i}\n"
        return self.show

class Main:
    """
    My first attempt at making a practical GUI app
    in OOP totally
    """
    def __init__(self):
        self.app = 0
        pass
    def Elements(self):
        self.app.Text_View(Process().run_process(), 0,0)
        pass
    def run(self):
        self.app = GUI()
        self.app.run_gui()
        self.Elements()
        self.app.mainloop()
    


if __name__ == "__main__":
    app = Main()
    app.run()