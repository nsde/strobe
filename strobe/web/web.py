import sys
import flask
import random

class Web:
    def __init__(self, title: str='Untitled', site: str='Strobe', preview: str='', port: int=1337):
        """A Flask webserver.

        Args:
            title (str, optional): Web page title. Defaults to 'Unnamed'.
            site (str, optional): Web page name. Defaults to 'Strobe'.
            preview (str, optional): Preview image for the website, can be an URL or internal path. Defaults to ''.
        """

        app = flask.Flask(__name__, static_url_path='/', template_folder='.')

        def page(text=''):
            return flask.render_template('index.html', title=title, site=site, preview=preview, buttons=self.buttons, text=text)
            
        @app.route('/', methods=['GET', 'POST'])
        def index():
            if flask.request.method == 'GET':
                return page()

            if flask.request.method == 'POST':
                for button in self.buttons:
                    if button['label'] == flask.request.form.to_dict().get('action'):
                        func = button['function']
                        response = func()
                        return page(text=str(response))

        @app.route('/stop')
        def stop():
            shutdown = flask.request.environ.get('werkzeug.server.shutdown')
            shutdown()

            return 'Stopping...'

        self.app = app
        self.port = port
        self.buttons = []

    def button(self, label: str='', *args, **kwargs):
        def inner(function):
            self.buttons.append({'label': label, 'function': function})

        return inner

    def start(self):
        self.app.run(port=self.port, debug=True)

if __name__ == '__main__':
    web = Web(title='Web Demo')

    @web.button(label='Say hi')
    def say_hi():
        return 'Hello there!'

    @web.button(label='Random number (1-10)')
    def random_number():
        return random.randint(1, 10)

    web.start()