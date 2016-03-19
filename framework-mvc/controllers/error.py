import core.web


class Controller:
    __WEB_ROOT = ""

    def __init__(self, WEB_ROOT):
        self.__WEB_ROOT = WEB_ROOT

    def index(self):
        import core
        error = core.web.get_url_data("code")
        if error is None:
            core.web.redirect_url(self.__WEB_ROOT + "error?code=404&url=" + core.web.current_url())
            SystemExit()
        import views.error as page
        page = page.content.format(**locals())
        return page
