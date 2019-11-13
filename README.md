Who Wrote This News Crawler
====================================================================================================
Web crawler for news articles from a subset of sources to power an open source news search engine.

<br>

Purpose
----------------------------------------------------------------------------------------------------
Used in "Machine Learning Techniques for Detecting Identifying Linguistic Patterns in the News Media" by [A Samuel Pottinger](https://gleap.org), web crawler parses RSS feeds from a list of news agencies, saving the articles found to a SQLite database.

<br>

Environment Setup
----------------------------------------------------------------------------------------------------
This requires Python 3 and pip to be installed for your platform. If available, run `$ pip install -r requirements.txt`.

<br>

Usage
----------------------------------------------------------------------------------------------------
These set of scripts are executable from the command line with `$ python news_crawler.py`. It will write to `articles.db` as a sqlite database in the same directory and expects the table to have been created using `create_table.sql`.

<br>

**Check robots.txt**  
This code base itself does not check for compliance with robots.txt on the target sites. In research, compliance with robots.txt was evaluated manually. Users of this code in the future should be sure to check continued compliance before use. See [sources.py](https://github.com/datadrivenempathy/who-wrote-this-news-crawler/blob/master/sources.py) for the URLs accessed.

<br>

Testing
----------------------------------------------------------------------------------------------------
Some automated tests are available and can be run with `$ nosetests`.

<br>

Development Standards
----------------------------------------------------------------------------------------------------
Please unit test and follow the [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html) where possible.

<br>

Related Projects
----------------------------------------------------------------------------------------------------
Note that this is in a series of related projects as linked:

 - [who-wrote-this-training](https://github.com/datadrivenempathy/who-wrote-this-training): logic for machine learning.
 - [who-wrote-this-server](https://github.com/datadrivenempathy/who-wrote-this-server): web application to demo the model.
 - [who-wrote-this-news-crawler](https://github.com/datadrivenempathy/who-wrote-this-news-crawler): crawler to record RSS feeds.

<br>

Open Source
----------------------------------------------------------------------------------------------------
This application's source is released under the [MIT License](https://opensource.org/licenses/MIT). The following open source libraries are used internally:

 - [requests](https://2.python-requests.org/en/master/) used under the [Apache v2 License](https://2.python-requests.org/en/master/user/intro/#apache2-license).
 - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) used under the [MIT License](https://code.launchpad.net/beautifulsoup).
 - [python_dateutil](https://dateutil.readthedocs.io/en/stable/) used under the [Apache v2 License](https://github.com/dateutil/dateutil/blob/master/LICENSE).
