# Copyright (c) 2014 Kohei Takahashi
#
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import gdb.printing

import boost.core
import boost.fusion

def register_boost_printers():
    gdb.printing.register_pretty_printer(None, boost.core.PP)
    gdb.printing.register_pretty_printer(None, boost.fusion.PP)
