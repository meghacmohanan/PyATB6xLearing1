
from abc import ABC, abstractmethod

class BrowserManager:
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        print("Browser stopped")

class ChromeBrowserManager(BrowserManager):
    def start(self):
        print("We are starting  Chrome browser")

ob= ChromeBrowserManager()
ob.start()
ob.stop()