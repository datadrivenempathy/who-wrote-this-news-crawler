"""Logic to interface with the articles sqlite database.

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
import os
import sqlite3


INSERT_SQL = '''
    INSERT INTO
        articles (
            source,
            sourceFeed,
            title,
            description,
            publishDate,
            crawlDate,
            link,
            author
        )
    VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
'''


def serialize_article_to_values(article):
    """Serialize an article to a list of values.

    Args:
        article: The article to be serialized.
    Returns:
        list of primitives that can be used with a DB API v2 compliant connection.
    """
    author = article.get_author()
    author_str = author if author else ''

    publish_date = article.get_publish_date()
    publish_date_str = publish_date.isoformat() if publish_date else ''

    crawl_date_str = article.get_crawl_date().isoformat()

    return [
        article.get_source(),
        article.get_source_feed(),
        article.get_title(),
        article.get_description(),
        publish_date_str,
        crawl_date_str,
        article.get_link(),
        author_str
    ]


def persist_articles(articles, target_db):
    """Persist articles to a given database.

    Args:
        articles: Iterable over Article to be saved.
        target_db: DB API v2 compliant connection to which the articles should be persisted.
    """
    cursor = target_db.cursor()

    for article in articles:
        article_values = serialize_article_to_values(article)
        cursor.execute(INSERT_SQL, article_values)

    target_db.commit()


def get_default_db():
    """Get the default database for the crawler.

    Returns:
        DB API v2 compliant connection to the crawler's default database.
    """
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    loc = os.path.join(parent_dir, 'articles.db')
    return sqlite3.connect(loc)
