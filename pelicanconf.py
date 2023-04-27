import os

AUTHOR = os.getenv('PELICAN_AUTHOR', 'author-test')
SITENAME = os.getenv('PELICAN_SITENAME', 'site-test')
SITEURL = ''

PATH = 'content'

TIMEZONE = os.getenv('PELICAN_TIMEZONE', 'Europe/Rome')

DEFAULT_LANG = os.getenv('PELICAN_LANG', 'fr')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

BIND = os.getenv('PELICAN_BIND', '127.0.0.1')
PORT = int(os.getenv('PELICAN_PORT', 8000))

THEME = '/opt/site-pelican/pelican-themes/'+os.getenv('PELICAN_THEME', 'basic')
print(THEME)
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True