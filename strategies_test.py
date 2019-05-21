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

import os
import unittest

import strategies


class StrategiesTest(unittest.TestCase):

    def test_npr(self):
        strategy = strategies.NprParseStrategy()
        self.__test_items(strategy, 'npr', True)

    def test_cnn(self):
        strategy = strategies.CnnParseStrategy()
        self.__test_items(strategy, 'cnn', False)

    def test_vox(self):
        strategy = strategies.VoxParseStrategy()
        self.__test_items(strategy, 'vox', True)

    def test_wsj(self):
        strategy = strategies.WsjParseStrategy('US Business')
        self.__test_items(strategy, 'wsj', False)

    def test_drudge(self):
        strategy = strategies.DrudgeReportParseStrategy()
        self.__test_items(strategy, 'drudge', False)

    def test_nyt(self):
        strategy = strategies.NewYorkTimesParseStrategy()
        self.__test_items(strategy, 'nyt', True)

    def test_bbc(self):
        strategy = strategies.BbcParseStrategy()
        self.__test_items(strategy, 'bbc', False)

    def test_breitbart(self):
        strategy = strategies.BreitbartParseStrategy()
        self.__test_items(strategy, 'breitbart', False)

    def test_breitbart(self):
        strategy = strategies.DailyMailParseStrategy()
        self.__test_items(strategy, 'dailymail', False)

    def test_fox(self):
        strategy = strategies.FoxParseStrategy()
        self.__test_items(strategy, 'fox', True)

    def __test_items(self, strategy, name, test_author):
        contents = self.__get_contents(name)
        items = strategy.get_items(contents)
        self.assertEquals(len(items), 1)

        self.assertEquals(strategy.get_title(items[0]), 'Test title')

        self.assertEquals(strategy.get_description(items[0]), 'Test description')

        self.assertEquals(strategy.get_publish_date(items[0]).year, 2019)
        self.assertEquals(strategy.get_publish_date(items[0]).month, 5)
        self.assertEquals(strategy.get_publish_date(items[0]).day, 20)

        self.assertEquals(strategy.get_link(items[0]), 'Test link')

        if test_author:
            self.assertEquals(strategy.get_author(items[0]), 'Test author')

    def __get_contents(self, name):
        parent_dir = os.path.dirname(os.path.realpath(__file__))
        examples_dir = os.path.join(parent_dir, 'rss_examples')

        filename = os.path.join(examples_dir, name + '.xml')
        with open(filename) as f:
            contents = f.read()

        return contents
