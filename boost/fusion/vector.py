# Copyright (c) 2015 Kohei Takahashi
#
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from boost.boost_gdb import register_pretty_printer
from boost.boost_gdb.utility import MemPrinter
from boost.fusion import PP, VOID_RE

import re as regex

def is_vector_data(field):
    return regex \
        .compile("^boost::fusion::vector_data\d+<.*>$") \
        .match(field.name)

@register_pretty_printer(PP)
class VectorPrinter:
    '''Print boost::fusion::vector'''

    name = 'vector'
    re = "^boost::fusion::vector\d*<.*>$"

    def __init__(self, val):
        self.val = val

    def _data_mem(self, data):
        f = data.type.fields()
        return reduce(MemPrinter().p, map(lambda x: str(data[x]), f), '')

    def to_string(self):
        type = VOID_RE.sub('', self.val.type.tag)
        vec = self.val
        for f in vec.type.fields():
            # val is a instance of vecotr<> if has vec member.
            if f.name == 'vec':
                vec = vec[f]
                break
        for f in vec.type.fields():
            if is_vector_data(f):
                return type + '{' + self._data_mem(vec[f]) + '}'

    def display_hint(self):
        return 'boost::fusion::vector'
