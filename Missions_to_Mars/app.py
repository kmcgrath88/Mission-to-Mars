from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    news_data = mongo.db.news_data.find_one()
    return render_template("index.html", news_data= news_data)


@app.route("/scrape")
def scraper():
    news_data  = mongo.db.news_data 
    news_data2 = mars_scrape.scrape()
    news_data.update({}, news_data2, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
