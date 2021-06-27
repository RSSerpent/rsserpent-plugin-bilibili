"""
This module contains a demonstration for creating RSS feeds from API data.

* We use `requests` to start an HTTP request;
* Then we use `response.json()` to retrieve data (typically in JSON format);
* Finally we transform such data to a dictionary,
  with all the necessary fields to create a RSS feed.
"""

import requests


path = "/example/api"


async def provider() -> dict:
    """Define an example data provider function, who will provide \
    the data needed by RSSerpent to create a RSS feed."""
    url = "https://httpbin.org/json"
    response = requests.get(url)
    data = response.json()
    # returns a dictionary compatible with `rsserpent.model.Feed`
    return {
        "title": data["slideshow"]["title"],
        "link": url,
        "description": data["slideshow"]["title"],
    }
