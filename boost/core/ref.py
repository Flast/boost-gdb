# Copyright (c) 2014 Kohei Takahashi
#
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from boost.boost_gdb import register_pretty_printer
from boost.core import PP

@register_pretty_printer(PP)
class RefPrinter:
    'Print boost::reference_wrapper'

    name = 'ref'
    re = "^boost::reference_wrapper<.*>$"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        type = self.val.type.tag
        ptr = self.val['t_']
        value = ptr.dereference()
        return type + '{*(' + str(ptr.type) + ')' + str(ptr) + ' = ' + str(value) + '}'

    def display_hint(self):
        return 'boost::reference_wrapper'
