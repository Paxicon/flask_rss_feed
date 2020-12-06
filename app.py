import os
import feedparser
import pymongo
from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId


urls = ["http://www.svt.se/nyheter/rss.xml", "http://www.dn.se/nyheter/m/rss/",
        "http://www.svd.se/?service=rss", "http://www.aftonbladet.se/rss.xml", "http://expressen.se/rss/nyheter", "http://api.sr.se/api/rss/program/83?format=145"]

feeds = [feedparser.parse(url) for url in urls]

# Feeds returns a list with nested multiple dictionaries inside it from the RSS feeds contained in the URL-list object. The template "rss_feed.html" handles iterating through it.


app = Flask(__name__)


@ app.route("/")
@ app.route("/read_feed")
def read_feed():
    return render_template("rss_feed.html", news=feeds)

# Add routing for a refresh routing function that checks feeds.etag and feeds.modified against the server and only updates accordingly


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=5000,
            debug=True)
