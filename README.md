# amazon-web-scraper

### Amazon eBook Scraper

Amazon eBook Web Scraper is a (hobbyist) web scraper written in Python 3, using the beautifulSoup library.

Using a single URL, it generates a full set of URLs and pulls data from a selected genre on the Amazon Kindle store (from 1-100), grabbing:
- Title
- Author
- Price
- Link
- ISBN

The backend is run on Flask and returned to the index site.

On the index site a front-end of jQuery and tablesorter JS library make a sortable HTML with the information.

**This is a hobbyist project and makes single requests which are not scheduled in advance.  This prevents load on Amazon's servers as their terms and conditions do not support remote Web Scrapers**
