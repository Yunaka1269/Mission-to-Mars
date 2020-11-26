# Mission-to-Mars

##Robin would like to adjust her web app to include all four of the hemisphere images and alter web design by using bootstrap. Modify scraping.py file so that click button will initiate chromedriver, splinter, and beautifulsoup to scrape full-image url and its title. 

###Resources
url:  
	
	https://mars.nasa.gov/news/
	
	https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
	
	http://space-facts.com/mars/
	
	https://mars.nasa.gov/insight/weather/
	
	https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars//

Software: 	

	Jupyter Notebook 6.1.4
	Visual Studio Code 1.51.1
  	ChromeDriver 86.0.4240.22
  	MongoDB v4.4.1
  
###Results:

On scraping.py file, we created a new function called hemisphere_data that will

  loop through individual hemisphere page by clicking <h3> title text in html
	
  find full resolution image url under <href> inside <a> tag with class "downloads"
	
  append both title and full-image url to the list 

inside index.html:

  use code {% for hemisphere in mars.hemisphere %}/{% endfor %} to make a loop to display all 4 images 

Bootstrap:

  style "Scrape New Data" button
  
  make all 4 pictures in horizontal thumbnails

###Summary

We can add other information text, table, images, and/or graph by targeting html tag/element and use Bootstrap to enhance webpage layout, theme, style, and responsiveness of device.
