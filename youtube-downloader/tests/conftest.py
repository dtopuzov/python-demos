import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdrivermanager import ChromeDriverManager


@pytest.fixture(scope="session")
def setup_browser():
    ChromeDriverManager().download_and_install()


@pytest.fixture
def browser():
    # Initialize the WebDriver instance
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True

    b = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)

    # Maximize
    b.maximize_window()

    # Make its calls wait for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
