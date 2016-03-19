print("Content-type: text/html")
content = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{{WEB_ROOT}}{{bundle[style]}}" />
        <title>Hello Python</title>
    </head>
    <body>
        <h1>special page : {name}</h1>
        Jonas
    </body>
</html>"""