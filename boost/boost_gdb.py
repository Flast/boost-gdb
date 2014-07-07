# Copyright (c) 2014 Kohei Takahashi
#
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import re

import gdb
from gdb.printing import PrettyPrinter
from gdb.printing import SubPrettyPrinter

class SubPrinter_Gen(SubPrettyPrinter):
    def __init__(self, printer):
        SubPrettyPrinter.__init__(self, printer.name)
        self.printer = printer
        self.regex = re.compile(printer.re)

    def __call__(self, val):
        return self.printer(val)

    def match(self, val):
        return None if val.type.tag == None else self.regex.match(val.type.tag)

class BoostPrettyPrinter_Gen(PrettyPrinter):
    def __init__(self, name):
        PrettyPrinter.__init__(self, name)
        self.subprinters = []

    def __call__(self, val):
        for sp in self.subprinters:
            if sp.match(val):
                return sp(val)
        return None

    def append(self, printer):
        self.subprinters.append(SubPrinter_Gen(printer))

def register_pretty_printer(Module):
    return lambda p: Module.append(p)
