# Copyright (c) 2015 Kohei Takahashi
#
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

class MemPrinter:
    delim = ''

    def tick(self):
        old = self.delim
        self.delim = ', '
        return old

    def p(self, l, r):
        return l + self.tick() + r
