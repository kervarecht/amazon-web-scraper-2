# amazon-web-scraper

### Amazon eBook Scraper

Amazon eBook Web Scraper is a (hobbyist) web scraper written in Python 3, using the beautifulSoup library.

Given a single, user-selected URL from the front-end (jQuery), it generates a full set of URLs and pulls data from a selected genre on the Amazon Kindle store (from 1-100), grabbing:
- Title
- Author
- Price
- ~~Link~~  (the links can be built directly off the ASIN, so there is no point to requesting both pieces of data)
- ASIN

The backend is run on Flask and returned to the index site.

On the index site a front-end of jQuery and tablesorter JS library make a sortable HTML with the information, dynamically updated with each new request.

The project's next step are:
- adjustable price range sliders on the front-end, showing only certain price ranges.
- deal picker on the back-end (user selects any number of genres and a certain price range, and is returned one book within that price range per genre).

**This is a hobbyist project and makes single requests which are not scheduled in advance.  This prevents load on Amazon's servers as their terms and conditions do not support remote Web Scrapers**
