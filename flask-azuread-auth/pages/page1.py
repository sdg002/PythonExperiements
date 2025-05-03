import os
import logging
from datetime import datetime
import dash
from dash import html

dash.register_page(__name__, title=f'Home ({os.environ.get("ENVIRONMENT")})')


def layout():
    logging.info('Page handler:{__name__}')
    html_elements = html.Div([
        html.H1('This is Page1'),
        html.Div(f'This is our Page1 content. {datetime.now()}'),
    ])
    return html_elements
