from env import ROOT_DIR

import os
import requests
import wget
import zipfile
from platform import system


chromedriver = "chromedriver"


def which_chromedriver():

    os = system()

    chromedrivers = {
        "Linux": "chromedriver_linux64.zip",
        "Darwin": "chromedriver_mac64.zip",
        "Windows": "chromedriver_win32.zip",
    }

    return chromedrivers[os]


def download_chromedriver():

    chromedriver_version = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").json()
    chromedriver_path = "http://chromedriver.storage.googleapis.com/{}/{}".format(chromedriver_version, which_chromedriver())
    extract_chromedriver(wget.download(chromedriver_path))


def extract_chromedriver(file):

    zip = zipfile.ZipFile(file)
    zip.extractall(ROOT_DIR)
    zip.close()

    os.remove(file)
    os.chmod(os.path.join(ROOT_DIR, chromedriver), 755)
