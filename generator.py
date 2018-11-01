# -*- coding: utf-8 -*-

from re import compile, findall
from random import randint, random
from mpmath import *


def parse_depth(num_length):
    grammar = {
        "<expr>": [
            "<func>",
            "<diff>",
            "<expr><op><expr>",
            "(<expr>)<op>(<expr>)",
            "<diff>",
            "<func>",
            "<expr><op><expr>",
            "<f>",
            "<diff>",
            "<expr><op>(<expr>)",
            "<func>",
            "<expr><op><expr>",
            "<diff>",
            "(<expr>)<op><expr>",
            "<diff>",
            "<expr><op><expr>",
            "<const>",
            "<diff>",
            "<func>",
            "<expr><op><expr>",
            "<diff>",
            "x",
            "<expr><op><expr>",
            "<func>",
        ],
        "<diff>": [
            'f(x).diff(x)'

        ],
        "<f>": [
            'f(x)'
        ],
        "<func>": [
            "log(<expr>,<log_constant>)",
            "pow(<expr>,<const>)",
            "sin(<expr>)",
            "cos(<expr>)",
            "acos(<expr>)",
            "asin(<expr>)",
            "atan(<expr>)"
        ],
        "<op>": [
            "+",
            "-",
            "*",
            "/",
        ],
        "<sign>": [
            "-",
            "+"
        ],
        "<const>": [
            "(<sign><const_float>)",
            "(<sign><const_int>)"

        ],
        "<const_float>": [
            "{}".format(round(random(),3)),
            "{}".format(round(mp.pi,3)),
            "{}".format(round(mp.degree,3)),
            "{}".format(round(mp.e,3)),
            "{}".format(round(mp.phi,3)),
            "{}".format(round(mp.euler,3)),
            "{}".format(round(mp.catalan,3)),
            "{}".format(round(mp.apery,3)),
            "{}".format(round(mp.khinchin,3)),
            "{}".format(round(mp.glaisher,3))

        ],
        "<const_int>": [
            "{}".format(randint(2,20))
        ],
        "<log_constant>":[
            "{}".format(round(mp.e,3)),"2","10"
        ]

    }

    length = num_length
    j = 0
    h = "<expr><op><expr>"

    s = r"<+[" + ('|'.join(list(map(lambda x: x[1:-1], grammar.keys())))) + "]+>"
    pattern = compile(s)

    # построение выражения вглубину
    while j < length:
        elems = pattern.findall(h)
        if not elems and j < length:
            break
        el = elems[0]
        new_el = grammar[el][randint(0,len(grammar[el])-1)]
        h = h.replace(el, new_el, 1)
        j += 1

    # убираем все оставишиеся нетерминальные символы
    while True:
        elements = pattern.findall(h)
        if elements:
            for el in elements:
                n = grammar["<const_float>"][randint(0, len(grammar["<const_float>"])-1)] \
                    if el == "<expr>" else grammar[el][randint(0, len(grammar[el])-1)]
                h = h.replace(el, n, 1)
        else:
            break

    return h