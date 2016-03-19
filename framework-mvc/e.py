#!/Programs/Python34/python

import cgi
import os
import core.web

WEB_ROOT = os.environ["SCRIPT_NAME"].replace("e.py", "")
ROOT = os.environ["SCRIPT_FILENAME"].replace("e.py", "")
getMethod = cgi.FieldStorage()
error = getMethod.getvalue("error")
current_url = core.web.current_url()
if error is None or error != int:
    core.web.redirect_url(WEB_ROOT+"error?code=404&url="+current_url)
elif error is int:
    core.web.redirect_url(WEB_ROOT+"error?code="+error+"&url="+current_url)
