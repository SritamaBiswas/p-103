import sys
import time
import random
import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
fromDirectory="C:/Users/LNMIIT/Downloads"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"hey,{event.src_path}has been created")
    def on_deleted(self, event):
        print(f"opps,{event.src_path}has been deleted")
    def on_modified(self, event):
        print(f"hey,{event.src_path}has been modified")
    def on_moved(self, event):
        print(f"someone moved{event.src_path} to{event.dest_path}")
eventHandler=FileEventHandler()
observer=Observer()
observer.schedule(eventHandler,fromDirectory,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stop")
    observer.stop()


