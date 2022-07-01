#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-07-01 13:25

@author: johannes
"""
from pathlib import Path
import sqlite3
import pandas as pd


def get_db_conn(db_path=None):
    """Return database connection."""
    if Path(str(db_path)).is_file():
        return sqlite3.connect(db_path)
    else:
        raise FileNotFoundError(
            f'Could not find the given database path. {db_path} '
            f'does not seem to be valid.'
        )


def get_dataframe(query=None, **kwargs):
    """Return dataframe.

    Initialize database connection and search using the given query.
    """
    if query:
        conn = get_db_conn(**kwargs)
        return pd.read_sql(query, conn)
