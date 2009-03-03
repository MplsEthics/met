"""
met/main.py - Minneapolis Ethics Training
"""

import pygtk
pygtk.require('2.0')
import met.window
import met.question

if __name__ == '__main__':
    try:
        met.window.Main()
    except KeyboardInterrupt:
        pass

