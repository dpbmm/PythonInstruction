#! /usr/bin/env python
# jira_io_support.py
# 2015.02.26

import os
import ast

def retrieve_bundle(filename='jira_ticket_bundle'):
    """Read and return a bundle of JIRA tickets.

    If the file is not found or is invalid, return None.
    """
    if os.path.exists(filename):
        with open('jira_ticket_bundle', 'r') as f:
            try:
                content = ast.literal_eval(f.read())
            except ValueError, SyntaxError:
                return
        return content

def save_bundle(bundle=None, filename='jira_ticket_bundle'):
    """Save a bundle of JIRA tickets; return filename used.

    If no bundle is received or bundle is invalid, return None."""
    try:
        # Validate bundle as argument to ast.literal_eval.
        bundle == ast.literal_eval(repr(bundle))
    except ValueError, SyntaxError:
        return
    if bundle:
        with open(filename, 'w') as f:
            f.write(repr(bundle))
        return filename
