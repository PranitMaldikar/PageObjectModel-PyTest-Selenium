from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

class TestData:

    load_dotenv()

    CHROME_EXECUTABLE_PATH = Service("C:\\Users\\prani\\Desktop\\Job grind\\pytest\\Portfolio-Test-Automator\\chromedriver.exe")
    BASE_URL = os.getenv("BASE_URL")   
    USER_NAME = os.getenv("USER_NAME")   
    PASSWORD = os.getenv("PASSWORD")   
    LOGIN_PAGE_TITLE = "HubSpot Login and Sign in"