print("Content-type: text/html")
content = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{{WEB_ROOT}}{{bundle[style]}}" />
        <title>Hello Python</title>
    </head>
    <body>
        <h1>From models : {error}</h1>
        <h1> Error </h1>
    </body>
</html>"""