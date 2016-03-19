
class Controller:
    def __init__(self):
        import views.home as page
        print(page.content)

    @staticmethod
    def index():
        import models.users as users
        user = users.Users
        name = user.name
        import views.home as page
        page = page.content.format(m=name)
        return page
