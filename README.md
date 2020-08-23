## web-scraping-challenge

# Mission to Mars
In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.<br>

## Step 1 - Scraping
-Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.<br>
-Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.<br>

### NASA Mars News
-Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.<br>

### JPL Mars Space Images - Featured Image
-Visit the url for JPL Featured Space Image here.<br>
-Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.<br>
-Make sure to find the image url to the full size .jpg image.<br>
-Make sure to save a complete url string for this image.<br>

### Mars Facts
-Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.<br>
-Use Pandas to convert the data to a HTML table string.<br>

### Mars Hemispheres
-Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.<br>
-You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.<br>
-Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.<br>
-Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.<br>

## Step 2 - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.<br>
-Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.<br>
-Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.<br>
--Store the return value in Mongo as a Python dictionary.<br>
-Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.<br>
-Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.<br>