from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
#display when we're looking at the home page, index.html
def index():
    #find the "mars" collection in our database
   mars = mongo.db.mars.find_one()
   #return an HTML template using an index.html file
   #, mars=mars) tells Python to use the "mars" collection in MongoDB
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   #assign a new variable that points to our Mongo database
   mars = mongo.db.mars
   #created a new variable to hold the newly scraped data
   #referencing the scrape_all function in the scraping.py file exported from Jupyter Notebook
   mars_data = scraping.scrape_all()
   #need to update the database using .update()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

if __name__ == "__main__":
   app.run()