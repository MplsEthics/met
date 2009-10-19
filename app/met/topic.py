#!/usr/bin/env python2.4

"""
Module to handler
"""

def get_topic(scenario_id):
    """This method helps format "Topic" strings consistently."""
    if scenario_id == 'coi1':
        return 'Topic One: Conflict of Interest, Part One'
    if scenario_id == 'coi2':
        return 'Topic One: Conflict of Interest, Part Two'
    if scenario_id == 'coi3':
        return 'Topic One: Conflict of Interest, Part Three'
    if scenario_id == 'coi4':
        return 'Topic One: Conflict of Interest, Part Four'
    if scenario_id == 'doi':
        return 'Topic Two: Disclosure of Information'
    if scenario_id == 'gift':
        return 'Topic Three: Gifts'
    return None

