"""Strategies for parsing different news feeds.

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

import bs4
import dateutil.parser

import util


class ParseStrategy:
    """Interface for RSS parsing strategies."""

    def get_source(self):
        """Get the name of news agency for which this strategy is intended.

        Returns:
            String name of the news source on whose RSS feed this strategy operates.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')

    def get_source_feed(self):
        """Get the URL of the RSS source feed.

        Returns:
            String URL at which the RSS feed can be found.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')

    def get_items(self):
        """Get the RSS items found.

        Returns:
            bs4.BeautifulSoup over the items found.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')

    def get_title(self, item):
        """Get the title of an article.

        Args:
            item: The bs4.BeautifulSoup over the item whose title should be returned.
        Returns:
            String title for this item.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')

    def get_description(self, item):
        """Get the description of an article.

        Args:
            item: The bs4.BeautifulSoup over the item whose description should be returned.
        Returns:
            String description for this item.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')

    def get_publish_date(self, item):
        """Get the publish date of an article.

        Args:
            item: The bs4.BeautifulSoup over the item whose publish date should be returned.
        Returns:
            Publish date as a datetime.datetime.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')

    def get_link(self, item):
        """Get the URL or link address for an article.

        Args:
            item: The bs4.BeautifulSoup over the item whose link should be returned.
        Returns:
            Link for the article.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')

    def get_author(self):
        """Get the author for an article.

        Args:
            item: The bs4.BeautifulSoup over the item whose author should be returned.
        Returns:
            The author of the article or None if not found.
        """
        raise NotImplementedError('Must use subclass of ParseStrategy.')


class NprParseStrategy(ParseStrategy):
    """Parse strategy for the NPR news feed."""

    def get_source(self):
        return 'NPR'

    def get_source_feed(self):
        return 'All Things Considered'

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'lxml')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        return item.find('description').contents[0]

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('pubdate').contents[0]
        )

    def get_link(self, item):
        return item.find('guid').contents[0]

    def get_author(self, item):
        author_selection = item.find('dc:creator')

        if author_selection:
            author = author_selection.contents[0]
        else:
            author = None

        return author


class CnnParseStrategy(ParseStrategy):
    """Parse strategy for the CNN news feed."""

    def get_source(self):
        return 'CNN'

    def get_source_feed(self):
        return 'Top Stories'

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        description_html = item.find('description').get_text()
        return bs4.BeautifulSoup(description_html, 'lxml').get_text()

    def get_publish_date(self, item):
        pub_date_selection = item.find('pubdate')
        if pub_date_selection:
            return dateutil.parser.parse(
                pub_date_selection.contents[0]
            )
        else:
            return None

    def get_link(self, item):
        return item.find('guid').contents[0]

    def get_author(self, item):
        author_selection = item.find('dc:creator')

        if author_selection:
            author = author_selection.contents[0]
        else:
            author = None

        return author


class VoxParseStrategy(ParseStrategy):
    """Parse strategy for the Vox news feed."""

    def get_source(self):
        return 'Vox'

    def get_source_feed(self):
        return ''

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'lxml')
        return soup.find_all('entry')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        content_html = item.find('content').contents[0]
        return bs4.BeautifulSoup(content_html, 'lxml').get_text()

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('published').contents[0]
        )

    def get_link(self, item):
        return item.find('id').contents[0]

    def get_author(self, item):
        return item.find('author').find('name').contents[0]


class WsjParseStrategy(ParseStrategy):
    """Parse strategy for the Wall Street Journal news feed."""

    def __init__(self, source_feed):
        """Create a new parse strategy for the Wall Street Journal.

        Args:
            source_feed: The name of the feed used.
        """
        ParseStrategy.__init__(self)
        self.__source_feed = source_feed

    def get_source(self):
        return 'Wall Street Journal'

    def get_source_feed(self):
        return self.__source_feed

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        return item.find('description').contents[0]

    def get_publish_date(self, item):
        date_str = item.find('pubdate').contents[0]
        date_str = date_str.replace('EST', '-05:00')
        date_str = date_str.replace('EDT', '-04:00')
        return dateutil.parser.parse(date_str)

    def get_link(self, item):
        return util.find_trailing_link(item)

    def get_author(self, item):
        return None


class DrudgeReportParseStrategy(ParseStrategy):
    """Parse strategy for the Drudge Report news feed."""

    def get_source(self):
        return 'Drudge Report'

    def get_source_feed(self):
        return ''

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'lxml')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        html_contents = item.find('description').contents[0]
        text = bs4.BeautifulSoup(html_contents, 'lxml').get_text()
        return text

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('dc:date').contents[0]
        )

    def get_link(self, item):
        return util.find_trailing_link(item)

    def get_author(self, item):
        return None


class NewYorkTimesParseStrategy(ParseStrategy):
    """Parse strategy for the New York Times news feed."""

    def get_source(self):
        return 'New York Times'

    def get_source_feed(self):
        return 'Homepage'

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'lxml')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        return item.find('description').contents[0]

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('pubdate').contents[0]
        )

    def get_link(self, item):
        return item.find('guid').contents[0]

    def get_author(self, item):
        author_selection = item.find('dc:creator')

        if author_selection:
            author = author_selection.get_text()
        else:
            author = None

        return author


class BbcParseStrategy(ParseStrategy):
    """Parse strategy for the BBC news feed."""

    def get_source(self):
        return 'BBC'

    def get_source_feed(self):
        return 'Top Stories'

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return list(filter(
            lambda x: x.find('title').contents != None,
            soup.find_all('item')
        ))

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        return item.find('description').get_text()

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('pubdate').contents[0]
        )

    def get_link(self, item):
        return item.find('guid').contents[0]

    def get_author(self, item):
        return None


class BreitbartParseStrategy(ParseStrategy):

    def get_source(self):
        return 'Breitbart'

    def get_source_feed(self):
        return ''

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        return item.find('description').get_text()

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('pubdate').contents[0]
        )

    def get_link(self, item):
        return item.find('guid').contents[0]

    def get_author(self, item):
        return item.find('author').contents[0]


class DailyMailParseStrategy(ParseStrategy):

    def get_source(self):
        return 'Daily Mail'

    def get_source_feed(self):
        return 'Homepage'

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        return item.find('description').get_text()

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('pubdate').contents[0]
        )

    def get_link(self, item):
        return item.find('guid').contents[0]

    def get_author(self, item):
        return None


class FoxParseStrategy(ParseStrategy):

    def get_source(self):
        return 'Fox'

    def get_source_feed(self):
        return 'Top News'

    def get_items(self, text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        return soup.find_all('item')

    def get_title(self, item):
        return item.find('title').contents[0]

    def get_description(self, item):
        return item.find('description').get_text()

    def get_publish_date(self, item):
        return dateutil.parser.parse(
            item.find('pubdate').contents[0]
        )

    def get_link(self, item):
        return item.find('guid').contents[0]

    def get_author(self, item):
        author_selection = item.find('dc:creator')

        if author_selection:
            author = author_selection.contents[0]
        else:
            author = None

        return author
