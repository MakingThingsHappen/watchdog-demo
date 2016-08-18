import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class FileModifiedEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        super(FileModifiedEventHandler, self).on_modified(event)
        if not event.is_directory and event.src_path.endswith('.py'):
            logging.info("Modified %s: %s", 'file', event.src_path)


if __name__ == "__main__":

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = FileModifiedEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
