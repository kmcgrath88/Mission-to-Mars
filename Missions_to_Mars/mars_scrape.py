#Import dependencies and setup
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

#Function to intialize brower
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

#Function to scrape information - similar steps to jupyter notebook
def scrape():
    mars_dict = {} #Create mars dictionary to return
    browser = init_browser()

    #####--NASA Mars New Site--#####
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1) #Allow page to load

    #Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get the latest news title and text
    news_data = {}
    article = soup.find('div', class_= 'list_text')
    news_data['article_title'] = article.find('a').text
    news_data['article_text'] = article.find('div', class_ = 'article_teaser_body').text
    mars_dict.update(news_data) #Add article title and text to Mars dictionary to return

    #####--JPL Mars Space Images - Featured Image--#####
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    html = browser.html
    soup = bs(html, 'html.parser')

    #Find image href
    image = soup.find('footer')
    image_url = image.a['data-fancybox-href']

    #Create image url
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url 
    mars_dict.update({'Mars_Image': featured_image_url}) #Add url to Mars dictionary to return

    #####--Mars Facts--#####
    mars_facts_url = 'https://space-facts.com/mars/'

    #Scrape the first table on the website
    mars_facts_table = pd.read_html(mars_facts_url)[0]

    #Rename the columns and set the index
    mars_facts_table_df = mars_facts_table.rename(columns={0: 'Description', 1: 'Mars'}) 
    mars_facts_table_df = mars_facts_table_df.set_index('Description')

    #Converting data to a html table string
    html_table = mars_facts_table_df.to_html(classes = 'table table-striped') 
    html_table = html_table.replace('\n', '')
    mars_dict.update({'Mars_Facts_Table': html_table}) #Add table to Mars dictionary to return

    #####--Mars Hemispheres--#####
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    #Create empty list
    hemisphere_image_urls = []

    #Links for hemispheres
    links = browser.find_by_css('a.product-item h3')

    #Loop through links, click link, find image url and title
    for m in range(len(links)):
        #Create empty dictionary for image urls and titles
        hemisphere = {}
        
        #Find elements on each loop
        browser.find_by_css('a.product-item h3')[m].click()
        
        #Find image url and get href
        hem_img_url = browser.links.find_by_text('Sample').first
        #Add image url to dictionary
        hemisphere['img_url'] = hem_img_url['href']
        
        #Get hemisphere title and add it to dictionary
        hemisphere['title'] = browser.find_by_css('h2.title').text
        
        #Add hemisphere dictionary to empty list
        hemisphere_image_urls.append(hemisphere)
        
        #Navigate back
        browser.back()

    mars_dict.update({'Hemispheres': hemisphere_image_urls}) #Add hemisphere_image_urls to Mars dictionary to return

    #Quit the browser after scraping
    browser.quit()

    #Return results
    return mars_dict



