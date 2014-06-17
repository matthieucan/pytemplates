#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(__file__))

from myproject.web import app

if __name__ == '__main__':
    app.run(debug=True)
