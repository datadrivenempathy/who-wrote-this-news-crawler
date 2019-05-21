"""Miscelanous utility functions.

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

import itertools


def flat_map(visitor, collection):
    """Flat map operation where returned iterables are flatted.

    Args:
        visitor: Function to apply.
        collection: The collection over which to apply the function.
    Returns:
        Flattened results of applying visitor to the collection.
    """
    return itertools.chain.from_iterable(
        map(visitor, collection)
    )


def find_trailing_link(item):
    """Parse a poorly formated trailing link.

    Args:
        item: The item as bs4.BeautifulSoup from which to get the link.
    Returns:
        The URL from the link.
    """
    contents = list(map(str, item.contents))

    link_found = False

    link_i = 0
    while not link_found:
        if contents[link_i].strip() == '<link/>':
            link_found = True
        else:
            link_i += 1

    link_text = item.contents[link_i + 1]
    return link_text.strip()
