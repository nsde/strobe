import sys
import flask
import requests

class Web:
    def __init__(self, title: str='Untitled', site: str='Strobe', preview: str=''):
        """A Flask webserver.

        Args:
            title (str, optional): Web page title. Defaults to 'Unnamed'.
            site (str, optional): Web page name. Defaults to 'Strobe'.
            preview (str, optional): Preview image for the website, can be an URL or internal path. Defaults to ''.
        """

        app = flask.Flask(__name__, static_url_path='/', template_folder='.')

        def page(text=''):
            return flask.render_template('index.html', title=title, site=site, preview=preview, buttons=self.buttons, text=text)
            
        @app.route('/')
        def index():
            return page()

        @app.route('/action/<label>')
        def action(label):
            for button in self.buttons:
                if button['label'] == label:
                    func = button['function']
                    response = func()
                    return page(text=response)

        @app.route('/stop')
        def stop():
            shutdown = flask.request.environ.get('werkzeug.server.shutdown')
            shutdown()

            return 'Stopping...'

        self.app = app
        self.buttons = []

    def button(self, label: str='', *args, **kwargs):
        def inner(function):
            self.buttons.append({'label': label, 'function': function})

        return inner

    def start(self):
        self.app.run(port=2077, debug=True)

if __name__ == '__main__':
    web = Web()
    
    @web.button(label='Say hi')
    def say_hi():
        return 'Hello there!'

    @web.button(label='Say bye')
    def say_bye():
        return 'Nice to meet you, bye!'

    web.start()