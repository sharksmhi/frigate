#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-07-01 13:39

@author: johannes
"""
from frigate import FilterOptions, get_data


if __name__ == '__main__':

    # Showcase of functionality for extracting database information.

    filter_opt = FilterOptions(
        year=['2020'],
        ship=['7798'],
    )
    df = get_data(
        db_path=r'C:\Arbetsmapp\datasets\PhysicalChemical\sharklog.db',
        template_name='archives.jinja',
        filter_obj=filter_opt
    )
    print(df)
