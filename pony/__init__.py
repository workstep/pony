from __future__ import absolute_import, print_function

import os, sys
from os.path import dirname

__version__ = 'p-0.7.1'

def detect_mode():
    try: import google.appengine
    except ImportError: pass
    else:
        if os.environ.get('SERVER_SOFTWARE', '').startswith('Development'):
            return 'GAE-LOCAL'
        return 'GAE-SERVER'

    try: mod_wsgi = sys.modules['mod_wsgi']
    except KeyError: pass
    else: return 'MOD_WSGI'

    if 'flup.server.fcgi' in sys.modules: return 'FCGI-FLUP'

    if 'uwsgi' in sys.modules: return 'UWSGI'

    try: sys.modules['__main__'].__file__
    except AttributeError:  return 'INTERACTIVE'
    return 'CHERRYPY'

MODE = detect_mode()

MAIN_FILE = None
for module_name, module in sys.modules.items():
    if module_name.startswith('_mod_wsgi_'):
        MAIN_FILE = module.__file__
        break

if MAIN_FILE is not None: MAIN_DIR = dirname(MAIN_FILE)
else: MAIN_DIR = None

PONY_DIR = dirname(__file__)
