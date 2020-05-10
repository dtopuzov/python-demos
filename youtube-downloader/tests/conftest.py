import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager


@pytest.fixture(scope="session")
def setup_browser():
    ChromeDriverManager().download_and_install()


@pytest.fixture
def browser():
    # Initialize the WebDriver instance
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('log-level=3')

    b = webdriver.Chrome(options=options)

    # Maximize
    b.maximize_window()

    # Make its calls wait for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
