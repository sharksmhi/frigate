#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-07-01 13:10

@author: johannes
"""
from .db import get_dataframe
from .filtering import FilterOptions  # noqa: F401

from pathlib import Path
from jinja2 import FileSystemLoader, Environment


_template_loader = FileSystemLoader(
    searchpath=Path(__file__).parent.joinpath('templates'))
TEMPLATES = Environment(loader=_template_loader)


def get_template(tmp_file):
    """Return jinja template."""
    return TEMPLATES.get_template(tmp_file)


def get_data(db_path=None, template=None, template_name=None, filter_obj=None,
             template_kwargs=None):
    """Return dataframe based on arguments.

    Loads jinja template and render with the input arguments.

    Args:
        db_path (str): Path to database (SQlite)
        template (jinja.Template): Render-ready template.
        template_name (str): Name of jinja template
        filter_obj (FilterOptions): Filter object. Contains information to
                                    render the template with.
        template_kwargs (dict): Arguments to pass on template rendering.
    """
    template = template or get_template(template_name)
    template_kwargs = template_kwargs or {}
    query = template.render(
        **template_kwargs,
        in_list_params=filter_obj.in_list_filter,
        not_in_list_params=filter_obj.not_in_list_filter
    )
    return get_dataframe(query=query, db_path=db_path)
