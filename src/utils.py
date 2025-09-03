import platform
import os
import json
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Config:
    def __init__(self):
        self.config_path = "config.json"
        self.RCM_username = ""
        self.RCM_password = ""
        self.monthly_util_delay = 0.5
    
    def loadConfig(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as file:
                    data = json.load(file)
                    self.RCM_username = data["RCM_username"]
                    self.RCM_password = data["RCM_password"]
                    self.monthly_util_delay = data["monthly_util_delay"]
            except: 
                self.defaultConfig()
        else:
            self.defaultConfig()

    def defaultConfig(self):
        print("> Creating default config.")
        config = {
            "RCM_username": "",
            "RCM_password": "",
            "monthly_util_delay": self.monthly_util_delay,
        }
        with open(self.config_path, "w") as file:
            json.dump(config, file)

def StartChromeDriver(start=False):    
    if(start):
        args = [
            ChromePath(),
            "--remote-debugging-port=9222",
            "--user-data-dir=C:\\selenium\\ChromeProfile",
            "--start-maximized",
            "--no-first-run",
            "--no-default-browser-check"
        ]
        subprocess.Popen(args)
        print("Started Chrome")
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)

    return driver

def ChromePath():

    system = platform.system()

    if system == "Windows":
        # Common paths for Chrome on Windows
        paths = [
            os.path.join(os.environ.get("ProgramFiles", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "Application", "chrome.exe")
        ]
    elif system == "Darwin":  # macOS
        paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
    elif system == "Linux":
        # Common paths for Chrome/Chromium on Linux
        paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser",
            "/opt/google/chrome/google-chrome"
        ]
    else:
        print(f"Unsupported operating system: {system}")
        return None

    for path in paths:
        if os.path.exists(path):
            return path
    return None