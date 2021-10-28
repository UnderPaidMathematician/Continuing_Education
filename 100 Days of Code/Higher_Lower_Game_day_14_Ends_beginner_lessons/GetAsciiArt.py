from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GetAsciiArt(text_to_convert):
    def __init__(self, text_to_convert):
        self.convertedText = text_to_convert.replace(" ", "%20")

    def openPage(self):
        browser = webdriver.Chrome('100 Days of Code\Higher_Lower_Game_day_14_Ends_beginner_lessons\chromedriver.exe')
        browser.get(f'http://patorjk.com/software/taag/#p=testall&f=Doom&t={self.convertedText}')


ascii_page = GetAsciiArt(text_to_convert="Test Art")

ascii_page.openPage()