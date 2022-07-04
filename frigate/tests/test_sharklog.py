#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-07-01 13:39

@author: johannes
"""
from pathlib import Path
from frigate import FilterOptions, get_data


if __name__ == '__main__':

    # Showcase of functionality for extracting database information.

    filter_opt = FilterOptions(
        year=['2019', '2020-2022'],
        ship=['34AR', '77KB', '77SE'],
        serno=['0-100'],
        proj=['BAS', 'SYK', 'IBT'],
        not_proj=['EXT']
    )
    df = get_data(
        db_path=str(Path(__file__).parent.joinpath('test_db/sharklog.db')),
        template_name='tmp_archives.jinja',
        filter_obj=filter_opt,
        template_kwargs=dict(
            table='sharkintlog',
            select_statement='distinct',
            field='archive_name'
        )
    )
    print(df)
