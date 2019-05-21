"""Template method pattern which can parse Article objects from an RSS feed.

----

Copyright 2019 Data Driven Empathy LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import datetime

import requests

import model


def transform_rss_item(item, strategy):
    """Transform a single RSS item.

    Args:
        item: The bs4.BeautifulSoup over the item to be transformed.
        strategy: The ParseStrategy by which to transform the given item.
    Returns:
        Newly created Article.
    """
    source = strategy.get_source()
    source_feed = strategy.get_source_feed()
    title = strategy.get_title(item)
    description = strategy.get_description(item)
    pubdate = strategy.get_publish_date(item)
    link = strategy.get_link(item)
    author = strategy.get_author(item)

    return model.Article(
        source,
        source_feed,
        title,
        description,
        pubdate,
        datetime.datetime.now(datetime.timezone.utc),
        link,
        author
    )


def parse(url, strategy):
    """Parse all items from a RSS feed using a given strategy.

    Args:
        url: String URL at which the RSS feed contents can be found.
        strategy: The ParseStrategy by which to gather Article objects from the given URL.
    Returns:
        List of model.Article.
    """
    rss = requests.get(url)
    items_raw = strategy.get_items(rss.text)
    return list(map(
        lambda item_raw: transform_rss_item(item_raw, strategy),
        items_raw
    ))
