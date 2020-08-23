from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    #@NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    news_data = {}
    #NASA Mars New Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get the latest news title
#     news_title = soup.find('div', class_='content_title').text

    
    #Get the paragraph text -- is this the teaser?
#     news_p = soup.find('div', class_ = 'article_teaser_body').text
    

    news_data['title'] = soup.find('div', class_='content_title').get_text()
    news_data['text'] = soup.find('div', class_ = 'article_teaser_body').get_text()

    # Quite the browser after scraping
    browser.quit()

    # Return results
    return news_data



