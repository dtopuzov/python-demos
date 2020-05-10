"""
This module contains YouTubeToMP3 abstraction.
"""
import os
from urllib import parse

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class YouTube320:
    # Locators
    GENERATE_BUTTON = (By.XPATH, "//*[@aria-controls='download']")
    DOWNLOAD_BUTTON = (By.XPATH, "//*[text()='Download MP3']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def download(self, youtube_url):
        # Open download page and search for video
        self.browser.get(youtube_url.replace("www.youtube", "www.320youtube"))

        # Generate link
        self.browser.find_element(*self.GENERATE_BUTTON).click()

        # Download
        wait = WebDriverWait(self.browser, 180)
        download = wait.until(expected_conditions.visibility_of_element_located(self.DOWNLOAD_BUTTON))
        link = download.get_attribute("href")

        # Wait until file is downloaded
        self.__download(link)

    @staticmethod
    def __download(link):
        out_dir = os.path.join(os.path.dirname(__file__), "..", "out")
        file_name = parse.unquote_plus(parse.unquote_plus(str(link.split("/")[-1]))).replace("&amp;", "&")
        for c in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
            file_name = file_name.replace(c, "")
        local_file = os.path.join(out_dir, file_name)

        with requests.get(link, stream=True) as r:
            r.raise_for_status()
            with open(local_file, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print("Downloaded: " + file_name)
