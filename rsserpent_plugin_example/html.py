"""
This module contains a demonstration for creating RSS feeds from HTML pages.

* We use `requests` to start an HTTP request;
* Then we use `response.text` to retrieve the HTML text;
* We need another library, `pyquery`, for parsing and querying HTML content.
  There are other popular choices, like `lxml` & `beautifulsoup4`, just
  choose one to your taste.
* Finally we transform the retrieved data to a dictionary,
  with all the necessary fields to create a RSS feed.
"""

import requests
from pyquery import PyQuery


path = "/example/html"


async def provider() -> dict:
    """Define an example data provider function, who will provide \
    the data needed by RSSerpent to create a RSS feed."""
    url = "https://httpbin.org/html"
    response = requests.get(url)
    d = PyQuery(response.text)
    # returns a dictionary compatible with `rsserpent.model.Feed`
    return {
        "title": d("h1").text(),
        "link": url,
        "description": d("div").text(),
    }
