from asyncio import events
from distutils import extension
import sys
import time
import random

import os
import shutil
from unicodedata import name

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "E:/Users/bhupi/Downloads"
to_dir = "H:/Download Test FIles"
print("Done !")
dir_tree = {
    "Image Files": ['.jpg', '.jpeg', '.png', '.jfif', '.gif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

list_of_file =  os.listdir(from_dir)

class FileMovementHandler(FileSystemEventHandler):
    def on_built(self, event):
        name, ext = os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            if ext in value:
                file_name = os.path.basename(event.src_path) 
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Moving Directory...  ")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)  
        print(event.src)
        print(event.src_path)

event_handler = FileMovementHandler()
observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

while True:
    time.sleep(2)
    print("PROCCESING...")




