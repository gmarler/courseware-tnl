'''
Create the scaffolding for a Flask-like framework.

>>> app = WebApp()
>>> @app.route("/")
... def index():
...     return 'Index Page'
...
>>> @app.route("/contact/")
... def contact():
...     return 'Contact Page'
...
>>> app.get("/")
'Index Page'
>>> app.get("/contact/")
'Contact Page'
>>> app.get("/no-such-page/")
'ERROR - no such page'


'''

# Write your code here:

class WebApp(object):
    def __init__(self):
        self.routes = dict()
    def route(self, url):
        def wrapper(func):
            self.routes[url] = func
            return func
        return wrapper
    def get(self, url):
        try:
            return self.routes[url]()
        except KeyError:
            return 'ERROR - no such page'
            

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
