import os
import feedparser
import pymongo
from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId

rss_data = feedparser.parse('http://www.svt.se/nyheter/rss.xml')

app = Flask(__name__)

print(rss_data.entries[0].title)


@app.route("/")
@app.route("/read_feed")
def read_feed():
    return render_template("rss_feed.html", news=rss_data.entries)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=5000,
            debug=True)
