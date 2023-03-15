from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Hello World! funciona por favor que tengo sueno v1.0'

if __name__ == '__main__':
    application.run()