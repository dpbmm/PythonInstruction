#! /usr/bin/env python
# jira_io_support.py
# 2015.02.26

import os
import ast

def retrieve_bundle(filename='jira_ticket_bundle'):
    """Read and return a bundle of JIRA tickets.

    If the file is not found, return None; if invalid, return False.
    """
    if os.path.exists(filename):
        try:
            with open('jira_ticket_bundle', 'r') as f:
                content = ast.literal_eval(f.read())
        except Exception:
            return False
        return content

def save_bundle(bundle=None, filename='jira_ticket_bundle'):
    """Save a bundle of JIRA tickets; return filename used.

    If no bundle is received, return None; if bundle invalid, return False.
    """
    try:
        # Validate bundle as argument to ast.literal_eval.
        if not bundle == ast.literal_eval(repr(bundle)):
            return False
    except Exception:
        return False
    if bundle:
        with open(filename, 'w') as f:
            f.write(repr(bundle))
        return filename
