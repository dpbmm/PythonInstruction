#! /usr/bin/env python
# jira.py
# MediaMath QA Python Class
# 20150304

"""Model simple JIRA functionality."""

import ast

possible_points = {None, 0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, float('inf')}

def get_summary():
    """Get non-empty summary string."""
    while True:
        summary = raw_input('Summary (required): ')
        if summary:
            break
    return summary

def get_is_open():
    """Get True or False (only) as 'is_open' state of ticket."""
    while True:
        is_open = raw_input('Open? (required) ')
        if is_open not in ['True', 'False']:
            print 'Please answer either True or False.'
        else:
            try:
                is_open = ast.literal_eval(is_open)
            except:
                print 'Please answer either True or False.'
                continue
            break
    return is_open

def get_points():
    """Get Agile point-value, validating before acceptance."""
    while True:
        points = raw_input('Points (optional): ')
        if points in ['None', '']:
            points = None
        elif points == '1/2':
            points = 0.5
        elif points == 'infinity':
            points = float('inf')
        else:
            try:
                points = int(points)
            except:
                print ('"{}" is not an integer and the program can\'t convert '
                'it to one.'.format(points))
                continue
        if points in possible_points:
            break
        else:
            print 'Please choose a valid point value.'
            continue
    return points

def get_assignee():
    # ask for assignee
    # check if assignee in data structure
    # if not, put assignee in
    # if in, return
    pass

def get_id():
    pass

def create_new():
    """Create new ticket."""
    summary = get_summary()
    is_open = get_is_open()
    points = get_points()
    assignee = get_assignee()
    ticket_id = get_id()

def report(id):
    """Report all information in a ticket, given ID number."""
    pass

def report_tickets(assignee):
    """Report all the tickets an assignee has, given assignee's name."""
    pass


