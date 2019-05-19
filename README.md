Scrapes VLIVE channel videos and displays them, for easier viewing

Usage:
Run `python scraper.py <url of channel videos page>` to create a videos.data file
Then run `python viewer_basic.py` to print out the data in ASCII
To view in a nicer format in a browser, run `FLASK_APP=viewer.py flask run`

Requirements: selenius and Flask
