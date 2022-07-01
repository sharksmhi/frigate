#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-07-01 14:26

@author: johannes
"""
from jinja2 import Template

QUERY_TEMPLATE = """
select {{select_statement}}
    {{field}}
from
    {{table}}
where
    1=1
    {% if in_list_params %}
        {% for key, list in in_list_params.items() %}
            and {{key}} in ( {{ "'" + "','".join(list) + "'" }} )
        {% endfor %}
    {% endif %}
    {% if not_in_list_params %}
        {% for key, list in not_in_list_params.items() %}
            and {{key}} not in ( {{ "'" + "','".join(list) + "'" }} )
        {% endfor %}
    {% endif %}
"""


if __name__ == '__main__':

    # Showcase of "manual" templating.

    sql_query = Template(QUERY_TEMPLATE).render(
        table='sharkintlog',
        select_statement='distinct',
        field='archive_name',
        in_list_params={'year': ['2021', '2022']}
    )
