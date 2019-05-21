"""Main entry point into the news crawler runnable from the CLI.

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

import persist
import sources
import template_method
import util


def process_source(source):
    """Process a single news source.

    Args:
        source: NewsSource instance describing the source whose RSS feed should be parsed.
    Returns:
        List of Article instances parsed.
    """
    url = source.get_url()
    strategy = source.get_parse_strategy()
    return template_method.parse(url, strategy)


def main():
    """Execute this script from the command line."""
    db = persist.get_default_db()
    articles = util.flat_map(process_source, sources.SOURCES)
    persist.persist_articles(articles, db)


if __name__ == '__main__':
    main()
