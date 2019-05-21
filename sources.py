"""List of sources to parse.

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

import strategies


class NewsSource:
    """Structure describing a single news source."""

    def __init__(self, url, parse_strategy):
        """Create a new news source.

        Args:
            url: String url at which the RSS feed contents can be found.
            parse_strategy: The strategy from strategies by which the RSS feed can be parsed.
        """
        self.__url = url
        self.__parse_strategy = parse_strategy

    def get_url(self):
        """Get the URL at which the RSS feed can be found.

        Returns:
            String url at which the RSS feed contents can be found.
        """
        return self.__url

    def get_parse_strategy(self):
        """Get the strategy by which this can be parsed.

        Returns:

        """
        return self.__parse_strategy


SOURCES = [
    NewsSource(
        'https://www.npr.org/rss/rss.php?id=2',
        strategies.NprParseStrategy()),
    NewsSource(
        'http://rss.cnn.com/rss/cnn_topstories.rss',
        strategies.CnnParseStrategy()),
    NewsSource(
        'https://www.vox.com/rss/index.xml',
        strategies.VoxParseStrategy()
    ),
    NewsSource(
        'https://feeds.a.dj.com/rss/RSSWorldNews.xml',
        strategies.WsjParseStrategy('World')
    ),
    NewsSource(
        'https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml',
        strategies.WsjParseStrategy('US Business')
    ),
    NewsSource(
        'https://feedpress.me/drudgereportfeed',
        strategies.DrudgeReportParseStrategy()
    ),
    NewsSource(
        'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
        strategies.NewYorkTimesParseStrategy()
    ),
    NewsSource(
        'http://feeds.bbci.co.uk/news/rss.xml',
        strategies.BbcParseStrategy()
    ),
    NewsSource(
        'http://feeds.feedburner.com/breitbart?format=xml',
        strategies.BreitbartParseStrategy()
    ),
    NewsSource(
        'https://www.dailymail.co.uk/home/index.rss',
        strategies.DailyMailParseStrategy()
    ),
    NewsSource(
        'http://feeds.foxnews.com/foxnews/latest',
        strategies.FoxParseStrategy()
    )
]
