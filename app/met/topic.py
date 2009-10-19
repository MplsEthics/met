#!/usr/bin/env python2.4

"""
Module to handler
"""

def get_topic(scenario_id):
    """This method helps format "Topic" strings consistently."""
    if 'coi' in scenario_id:
        return 'Topic 1'
    if 'doi' in scenario_id:
        return 'Topic 2'
    if 'gift' in scenario_id:
        return 'Topic 3'

