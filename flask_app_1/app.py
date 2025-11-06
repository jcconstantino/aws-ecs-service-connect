from datetime import datetime

import requests

from . import create_app
from dotenv import load_dotenv
import os

load_dotenv('../default.env')

flask_app = create_app()


@flask_app.route('/')
def hello() -> str:
    ''' Return a friendly HTTP greeting '''
    return f'Hello, World from flask app 1! THIS IS SMALL MODIFICATION! :) Time is {datetime.now()}'


@flask_app.route('/get_message')
def get_message() -> str:
    ''' endpoint to test AWS ECS Service Connect functionality across services '''
    #url = f'http://flask_app_2:{os.environ["PORT_FLASK_APP_2"]}/return_message'  # local testing with docker-compose
    url = f'http://service-connect-demo-service-2:{os.environ["PORT_FLASK_APP_2"]}/return_message'
    print(f'trying url: {url}')
    message = requests.get(url, timeout=10)

    return message.text


@flask_app.route('/get_message_across_cluster')
def get_message_across_cluster() -> str:
    ''' endpoint to test AWS ECS Service Connect functionality across clusters '''
    #url = f'http://flask_app_3:{os.environ["PORT_FLASK_APP_3"]}/return_message'  # local testing with docker-compose
    url = f'http://service-connect-demo-service-3:{os.environ["PORT_FLASK_APP_3"]}/return_message'
    print(f'trying url: {url}')
    message = requests.get(url, timeout=10)

    return message.text

# if __name__ == '__main__':
#     flask_app.run(host='0.0.0.0')
