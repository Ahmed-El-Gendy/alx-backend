#!/usr/bin/env python3
"""
function named index_range
"""


def index_range(page, page_size):
    """
    return a tuple containing a start and end index
    """
    val = (page - 1) * page_size, ((page - 1) * page_size) + page_size
    return val
