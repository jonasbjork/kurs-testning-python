#!/usr/bin/env python

import requests
import re
import os
import tarfile
import shutil
from urllib.request import urlopen
import bz2

def download_geckodriver():
    # Get latest geckodriver version
    response = requests.head(
        'https://github.com/mozilla/geckodriver/releases/latest',
        allow_redirects=True
    )
    
    version = re.search(r'v\d+\.\d+\.\d+', response.url)
    geckodriver_version = version.group(0) if version else None

    if not geckodriver_version:
        raise Exception("!!! Could not determine geckodriver version")
    
    print(f"--- Found latest geckodriver version: {geckodriver_version}")
    
    # Download and install
    url = f"https://github.com/mozilla/geckodriver/releases/download/{geckodriver_version}/geckodriver-{geckodriver_version}-linux64.tar.gz"
    filename = f"geckodriver-{geckodriver_version}-linux64.tar.gz"
    
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            f.write(r.content)
    
    print(f"--- Downloaded {filename}")

    with tarfile.open(filename, 'r:gz') as tar:
        tar.extractall('/usr/local/bin')
    
    os.chmod('/usr/local/bin/geckodriver', 0o755)
    os.remove(filename)

    print("--- Geckodriver installed successfully to /usr/local/bin/geckodriver")

def install_firefox():
    firefox_setup = "firefox-setup.tar.bz2"
    
    print(f"--- Downloading latest Firefox setup : [ {firefox_setup} ]")
    with urlopen('https://download.mozilla.org/?product=firefox-latest&os=linux64') as response:
        with open(firefox_setup, 'wb') as f:
            f.write(response.read())
    
    print(f"--- Downloaded Firefox setup to {firefox_setup}")

    with tarfile.open(firefox_setup, 'r:bz2') as tar:
        tar.extractall('/opt/')
    
    os.symlink('/opt/firefox/firefox', '/usr/bin/firefox')
    os.remove(firefox_setup)

if __name__ == "__main__":
    download_geckodriver()
    install_firefox()
