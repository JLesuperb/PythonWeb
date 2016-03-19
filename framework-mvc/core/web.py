import os
import urllib.parse

bundles = {
    "style": "bundles/css/style.css"
}


def redirect_url(url):
    print("Status: 301 Moved Permanently")
    print("Location:" + url)
    print("Content-type: text/html")
    print()


def current_url():
    return "http://" + os.environ["SERVER_NAME"] + os.environ["REQUEST_URI"]


def get_url_data(name):
    parsed = urllib.parse.urlparse(current_url())
    if parsed.query is None or parsed.query == "":
        return None
    if urllib.parse.parse_qs(parsed.query)[name] is None:
        return None
    else:
        return urllib.parse.parse_qs(parsed.query)[name][0]
