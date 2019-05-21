"""Copyright 2019 Data Driven Empathy LLC

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
import sqlite3
import unittest

import dateutil.parser

import model
import persist


class PersistTest(unittest.TestCase):

    def setUp(self):
        self.__connection = sqlite3.connect(':memory:')
        cursor = self.__connection.cursor()
        cursor.execute('''
            CREATE TABLE "articles" (
                `source` TEXT,
                `sourceFeed` TEXT,
                `title` TEXT,
                `description` TEXT,
                `publishDate` TEXT,
                `crawlDate` TEXT,
                `link` TEXT,
                `author` TEXT
            )
        ''')
        self.__connection.commit()
        self.__test_article = model.Article(
            'source 1',
            'source.feed',
            'title 1',
            'description 1',
            dateutil.parser.parse('2019-05-20T23:37:37.294816Z'),
            dateutil.parser.parse('2019-05-21T23:37:37.294816Z'),
            'test link',
            'test author'
        )

        self.__test_articles = [ self.__test_article ]

    def tearDown(self):
        cursor = self.__connection.cursor()
        cursor.execute(''' DROP TABLE "articles" ''')
        self.__connection.commit()

    def test_serialize_article_to_values(self):
        values = persist.serialize_article_to_values(self.__test_article)
        self.assertEquals(len(values), 8)
        self.assertEquals(values[2], 'title 1')

    def test_persist_articles(self):
        persist.persist_articles(self.__test_articles, self.__connection)
        cursor = self.__connection.cursor()
        cursor.execute('''SELECT title FROM articles''')
        results = cursor.fetchone()
        self.assertEquals(results[0], 'title 1')
