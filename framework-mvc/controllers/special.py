
class Controller:
    def __init__(self):
        import views.home as page
        print(page.content)

    @staticmethod
    def index(name):
        import views.special as page
        name = name
        page = page.content.format(**locals())
        return page
