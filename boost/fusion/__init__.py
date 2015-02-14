# Copyright (c) 2015 Kohei Takahashi
#
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

from boost.boost_gdb import BoostPrettyPrinter_Gen

PP = BoostPrettyPrinter_Gen('boost.fusion')

import re

VOID_RE = re.compile("(?:, boost::fusion::void_)+")


import boost.fusion.vector
