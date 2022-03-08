# e_ink_display
Personal E-Ink display


This collection of code runs a Pimoroni 7 color e-ink display. There are four individual pages that can be accessed:
* News: Data from the New York Times API and displayed through a flask application
* Weather: Data from open weather API and displayed through the same flask application
* Images: TBD
* Stock Data: TBD

## Flask Application 

The way the news and weather data are displayed is a screenshot of a flask webpage. 

The API keys need to be saved as designated text files in the keys folder

Then running get_data will update the json files that house the data

After that, you can start running the flask application

Finally, using the html.sh bash file and specifying the URL, you can toggle between the two pages

The news page displays a random article from the new york times top articles at the time of the data request
including the title, abstract, image, and a qr code to link of the article 

The weather page displays the current weather at the time of the request as well as a 5 day forecast


To do:
* have the get_data.py function to run every hour 
* be able to hook up the functions to a button that will automatically refresh page to news or weather


