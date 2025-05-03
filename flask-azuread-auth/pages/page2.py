import os
import logging
from datetime import datetime
import dash
from dash import html

dash.register_page(__name__, title=f'Page2 ({os.environ.get("ENVIRONMENT")})')


def layout():
    logging.info('Page handler:{__name__}')
    html_elements = html.Div([
        html.H1('This is Page2'),
        html.Div(f'This is our Page2 content. {datetime.now()}'),
    ])
    return html_elements
