#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import codecs
import sys
import pkgutil
from os import path

from tatsu import parse
from .semantics import ANTLRSemantics


def antlr_grammar():
    return str(pkgutil.get_data(__name__, 'antlr.ebnf'), 'utf-8')


def translate(filename, trace):
    with codecs.open(filename) as f:
        text = f.read()
    gname = path.splitext(path.basename(filename))[0].capitalize()
    semantics = ANTLRSemantics(gname)
    model = parse(
        antlr_grammar(),
        text,
        name=gname,
        filename=filename,
        semantics=semantics,
        trace=trace
    )
    print(model)


def main():
    if len(sys.argv) < 2:
        thisprog = path.basename(sys.argv[0])
        print(thisprog)
        print('Usage:')
        print('\t', thisprog, 'FILENAME.g [--trace]')
        sys.exit(1)
    translate(sys.argv[1], '--trace' in sys.argv or '-t' in sys.argv)


if __name__ == '__main__':
    main()
