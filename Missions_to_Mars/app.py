#Import dependencies and setup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape #Bringing in mars_scrape.py file

app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars_app" 
mongo = PyMongo(app)

#Creating app route / and defining function
@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data = mars_data)

#Creating app route /scrape and defining function
@app.route("/scrape")
def scraper():
    mars_data  = mongo.db.mars_data 
    mars_data2 = mars_scrape.scrape() # automatically equal to what scrape() returns -- double check this
    mars_data.update({}, mars_data2, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
