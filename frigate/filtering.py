#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-07-01 13:10

@author: johannes
"""
from typing import Optional
from dataclasses import dataclass
from functools import cached_property


@dataclass
class FilterOptions:
    """Class for keeping track of filter options."""

    cdi: Optional[list] = None
    ship: Optional[list] = None
    year: Optional[list] = None
    serno: Optional[list] = None
    seqno: Optional[list] = None
    proj: Optional[list] = None
    not_proj: Optional[list] = None
    orderer: Optional[list] = None
    not_orderer: Optional[list] = None

    def get_list(self, value_list, key=None):
        """Return list of all filter values."""
        if not value_list:
            return
        key = key or ''
        _list = []
        for v in value_list:
            if isinstance(v, str):
                if '-' in v:
                    _list.extend(self.get_intervals(*v.split('-')))
                else:
                    _list.append(v)
            else:
                _list.extend(v)
        if 'serno' in key:
            _list = [x.zfill(4) for x in _list]
        return _list

    @staticmethod
    def get_intervals(x1, x2):
        """Return list of all numbers between a given start and end value."""
        return list(map(str, range(int(x1), int(x2) + 1)))

    @cached_property
    def in_list_filter(self):
        """Return filter dictionary.

        Dictionary of "in-list" filter fields including the
        corresponding values.
        """
        return {
            k: self.get_list(getattr(self, k), key=k)
            for k in self.active_fields if not k.startswith('not_')
        }

    @cached_property
    def not_in_list_filter(self):
        """Return filter dictionary.

        Dictionary of "not-in-list" filter fields including the
        corresponding values.
        """
        return {
            k.replace('not_', ''): self.get_list(getattr(self, k), key=k)
            for k in self.active_fields if k.startswith('not_')
        }

    @cached_property
    def active_fields(self):
        """Return a set of the activated filter fields."""
        return set([k for k, v in self.__dict__.items() if v])
