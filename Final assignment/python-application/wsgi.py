#!/usr/bin/env python
"""
exports the app instance.
"""

from config import configs  # side effect
import os
from app import create_app

app_mode = None
try:
    app_mode = os.environ['FLASK_ENV']
    app_config = configs[app_mode]
except KeyError:
    print(f"Set the FLASK_ENV environmental variable to one of [{','.join(configs.keys())}]")
    exit(1)

# the Flask app instance
app = create_app(app_config)


@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
