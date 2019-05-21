"""Data structures supporting the who wrote this news crawler.

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

class Article:
    """Data structure describing an article."""

    def __init__(self, source, source_feed, title, description, publish_date,
        crawl_date, link, author):
        """Create a new article record.

        Args:
            source: The name of the agency that published this article.
            source_feed: The name for the RSS feed, helping disambiguate if there are many.
            title: The title for the article.
            description: The description for the article.
            publish_date: The datetime.datetime for when this article was published.
            crawl_date: The datetime.datetime for when this article was crawled.
            link: URL where the full article can be found.
            author: The author of the article.
        """

        self.__source = source
        self.__source_feed = source_feed
        self.__title = title
        self.__description = description
        self.__publish_date = publish_date
        self.__crawl_date = crawl_date
        self.__link = link
        self.__author = author

    def get_source(self):
        """Get the name of the agency that published this article.

        Returns:
            The name of the agency that published this article like NPR.
        """
        return self.__source

    def get_source_feed(self):
        """Get the bame for the RSS feed in which this application was found.

        Returns:
            The string name for the RSS feed, helping disambiguate if there are many.
        """
        return self.__source_feed

    def get_title(self):
        """Get the text of the article title.

        Returns:
            The title for the article as a string.
        """
        return self.__title

    def get_description(self):
        """Get the description contents for this article.

        Returns:
            The description for the article as a string.
        """
        return self.__description

    def get_publish_date(self):
        """Get the datetime for when this article was published.

        Returns:
            The datetime.datetime for when this article was published.
        """
        return self.__publish_date

    def get_crawl_date(self):
        """Get the datetime for when this article was crawled.

        Returns:
            The datetime.datetime for when this article was crawled.
        """
        return self.__crawl_date

    def get_link(self):
        """Get the URL at which the full article can be found.

        Returns:
            URL where the full article can be found.
        """
        return self.__link

    def get_author(self):
        """Get the name of the author if provided.

        Returns:
            The author of the article as a string. None if no author given.
        """
        return self.__author
