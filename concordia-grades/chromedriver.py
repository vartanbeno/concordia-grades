from env import ROOT_DIR

import os
import requests
import wget
import zipfile
from platform import system
from selenium.webdriver.chrome.options import Options


chromedriver = "chromedriver"
chromedriver_path = os.path.join(ROOT_DIR, chromedriver)

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")


def chromedriver_exists():

    return os.path.exists(chromedriver_path)


def which_chromedriver():

    os = system()

    chromedrivers = {
        "Linux": "chromedriver_linux64.zip",
        "Darwin": "chromedriver_mac64.zip",
        "Windows": "chromedriver_win32.zip",
    }

    return chromedrivers[os]


def download_chromedriver():

    if not chromedriver_exists():
        chromedriver_version = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").json()
        chromedriver_path = "http://chromedriver.storage.googleapis.com/{}/{}".format(chromedriver_version, which_chromedriver())
        extract_chromedriver(wget.download(chromedriver_path))
        print()
    else:
        print("{} already exists in this directory.".format(chromedriver))


def extract_chromedriver(file):

    zip = zipfile.ZipFile(file)
    zip.extractall(ROOT_DIR)
    zip.close()

    os.remove(file)
    os.chmod(os.path.join(ROOT_DIR, chromedriver), 755)
