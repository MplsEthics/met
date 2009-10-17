import os
import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from met import content
from met import session

from fallback import Fallback
from main import Main
from reset import Reset
from scenario import Scenario

# define the navigation view order
order = [
    'main',
    'instr1',
    'instr2',
    'over1',
    'over2',

    # intrduce topic 1: conflict of interest
    'topic1',

    # conflict of interest part 1
    'coi1/intro',
    'coi1/scenario',
    'coi1/disc1',
    'coi1/disc2',

    # conflict of interest part 2
    'coi2/intro',
    'coi2/scenario',
    'coi2/disc1',
    'coi2/disc2',
    'coi2/disc3',

    # conflict of interest part 3
    'coi3/intro',
    'coi3/scenario',
    'coi3/disc1',
    'coi3/disc2',
    'coi3/disc3',

    # conflict of interest part 4
    'coi4/intro',
    'coi4/scenario',
    'coi4/disc1',

    # disclosure of information
    'doi/intro',
    'doi/scenario',
    'doi/disc1',

    # gifts
    'gifts/intro1',
    'gifts/intro2',
    'gifts/scenario',
    'gifts/disc1',

    # ethics report line & contact info
    'reportline1',
    'reportline2',
    'reportline3',

    'contacts',
    'congrats',
    'certificate',
]

