import os
import pdb
import sys


def debug():
    for attr in ('stdin', 'stdout', 'stderr'):
        setattr(sys, attr, getattr(sys, '__%s__' % attr))
    pdb.set_trace()

content_dir = os.path.join(os.path.dirname(__file__), '../../content')
