from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

#Create an instance of Flask  --- separate app.py file???
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app") ---- do i need this?



def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    data_dict = {} # --- create dictionary
    browser = init_browser()

    #NASA Mars New Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get the latest news title and text
    news_data = {}
    article = soup.find('div', class_= 'list_text')
    news_data['article title'] = article.find('a').text
    news_data['article text'] = article.find('div', class_ = 'article_teaser_body').text
    data_dict.update(news_data)
    # news_title = article.find('a').text 
    # news_p = article.find('div', class_ = 'article_teaser_body').text
    
    #JPL Mars Space Images - Featured Image
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    html = browser.html
    soup = bs(html, 'html.parser')

    image = soup.find('footer')
    image_url = image.a['data-fancybox-href']

    featured_image_url = 'https://www.jpl.nasa.gov' + image_url # --- add to dictionary??
    data_dict.update({'Mars Image': featured_image_url})

    #Mars Facts
    mars_facts_url = 'https://space-facts.com/mars/'

    mars_facts_table = pd.read_html(mars_facts_url)[0]

    mars_facts_table_df = mars_facts_table.rename(columns={0: 'Description', 1: 'Mars'}) 
    mars_facts_table_df = mars_facts_table_df.set_index('Description')

    html_table = mars_facts_table_df.to_html() # --- add to dictionary??
    data_dict.update({'Mars Facts Table': html_table})

    # html_table.replace('\n', '')
    # df.to_html('table.html')

    #Mars Hemispheres
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    hemisphere_image_urls = []

    #Get list of all hemispheres
    links = browser.find_by_css('a.product-item h3')

    #Loop through links, click link, find image url and title
    for m in range(len(links)):
        hemisphere = {}
        
        #Find elements on each loop
        browser.find_by_css('a.product-item h3')[m].click()
        
        #Find image url and get href
        hem_img_url = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = hem_img_url['href']
        
        #Get hemisphere title
        hemisphere['title'] = browser.find_by_css('h2.title').text
        
        #Add hemisphere dictionary to list
        hemisphere_image_urls.append(hemisphere)
        
        #Navigate back
        browser.back()

        # Quite the browser after scraping
    data_dict.update({'Hemisphers': hemisphere_image_urls})
    browser.quit()

    # Return results
    return data_dict



