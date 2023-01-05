import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from printer import print_file

if __name__ == "__main__":
    observer = Observer()
    # watch the upload folder for pdf files
    handler = PatternMatchingEventHandler(
        patterns=["*.pdf"], ignore_directories=True, case_sensitive=False)
    observer.schedule(handler, path='./upload', recursive=False)
    # define the callback function

    def on_created(event):
        print("File created: ", event.src_path)
        # print the file
        print_file(event.src_path)

    # register the callback function
    handler.on_created = on_created

    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
