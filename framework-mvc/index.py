#!/Programs/Python34/python
import cgi
import os
import cgitb
import sys
from importlib.machinery import SourceFileLoader
import core.web as web

cgitb.enable()

WEB_ROOT = os.environ["SCRIPT_NAME"].replace("index.py", "")
ROOT = os.environ["SCRIPT_FILENAME"].replace("index.py", "")
getMethod = cgi.FieldStorage()
cmd = getMethod.getvalue("cmd")
html = ""
if cmd is None:
    file = SourceFileLoader("home", "controllers/home.py").load_module()
    controller = file.Controller
    html = controller.index()
else:
    params = getMethod.getvalue("cmd").split('/')
    error_d = ROOT + "controllers/" + params[0] + ".py"
    if params[0] != "" and params[0] != "error" and os.path.exists(ROOT + "controllers/" + params[0] + ".py"):
        controller = params[0]
        file = SourceFileLoader(params[0], "controllers/" + params[0] + ".py").load_module()
        controller = file.Controller
        html = controller.index()
    elif params[0] != "" and params[0] != "error":
        file = SourceFileLoader("special", "controllers/special.py").load_module()
        controller = file.Controller
        html = controller.index(params[0])
    else:
        file = SourceFileLoader("error", "controllers/error.py").load_module()
        controller = file.Controller(WEB_ROOT)
        # controller.WEB_ROOT = WEB_ROOT
        html = controller.index()

html = html.format(bundle=web.bundles, **locals())
print(html)
