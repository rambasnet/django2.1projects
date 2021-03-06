from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    return HttpResponse('Hello there wonderful world...')

def bye(request):
    return HttpResponse('Adios...until next time...')


def current_datetime(request):
    now = datetime.datetime.now()
    html = '''<!DOCTYPE html>
            <html>
            <head>
                <title>Current Server Datetime</title>
                <style>
                    body {{
                        background-color: lightblue;
                    }}
                    p {{
                        font-size: 1.5em;
                        color: green;
                    }}
                </style>
            </head>
            <body>
                <h1>{}</h1>
                <p>It is now {}.</p>
            </body>
            </html>
            '''.format('Date Time', now)
    return HttpResponse(html)

    
def logout(requst):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    <style>
        body {{
            background-color: lightblue;
        }}
        h1 {{
            color: white;
            text-align: center;
        }}
        p {{
            font-family: verdana;
            font-size: 20px;
        }}
    </style>
    </head>
    <body>

    <h1>{}</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>
    '''.format('This is heading!')
    return HttpResponse(html)