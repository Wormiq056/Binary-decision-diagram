#
# simpleBool.py
#
# Example of defining a boolean logic parser using
# the operatorGrammar helper method in pyparsing.
#
# In this example, parse actions associated with each
# operator expression will "compile" the expression
# into BoolXXX class instances, which can then
# later be evaluated for their boolean value.
#
# Copyright 2006, by Paul McGuire
# Updated 2013-Sep-14 - improved Python 2/3 cross-compatibility
# Updated 2021-Sep-27 - removed Py2 compat; added type annotations
#
from typing import Callable, Iterable

from pyparsing import infixNotation, opAssoc, Keyword, Word, alphas, ParserElement

import sys

ParserElement.enablePackrat()


# define classes to be built at parse time, as each matching
# expression type is parsed
class BoolOperand:
    def __init__(self, t):
        self.label = t[0]
        self.value = eval(t[0])

    def __bool__(self) -> bool:
        return self.value

    def __str__(self) -> str:
        return self.label

    __repr__ = __str__


class BoolNot:
    def __init__(self, t):
        self.arg = t[0][1]

    def __bool__(self) -> bool:
        v = bool(self.arg)
        return not v

    def __str__(self) -> str:
        return "~" + str(self.arg)

    __repr__ = __str__


class BoolBinOp:
    repr_symbol: str = ""
    eval_fn: Callable[[Iterable[bool]], bool] = lambda _: False

    def __init__(self, t):
        self.args = t[0][0::2]

    def __str__(self) -> str:
        sep = " %s " % self.repr_symbol
        return "(" + sep.join(map(str, self.args)) + ")"

    def __bool__(self) -> bool:
        return self.eval_fn(bool(a) for a in self.args)


class BoolAnd(BoolBinOp):
    repr_symbol = "&"
    eval_fn = all


class BoolOr(BoolBinOp):
    repr_symbol = "|"
    eval_fn = any


# define keywords and simple infix notation grammar for boolean
# expressions
TRUE = Keyword("True")
FALSE = Keyword("False")
NOT = Keyword("not")
AND = Keyword("and")
OR = Keyword("or")
boolOperand = TRUE | FALSE | Word(alphas, max=1)
boolOperand.setParseAction(BoolOperand).setName("bool_operand")

# define expression, based on expression operand and
# list of operations in precedence order
boolExpr = infixNotation(
    boolOperand,
    [
        (NOT, 1, opAssoc.RIGHT, BoolNot),
        (AND, 2, opAssoc.LEFT, BoolAnd),
        (OR, 2, opAssoc.LEFT, BoolOr),
    ],
).setName("boolean_expression")


def parse_bfunc(bFunc: str):
    # AB+B!C
    # test_string = "A and not B and C or not A and C and not B"

    terms = bFunc.split("+")
    formatted_terms = []
    for term in terms:
        i = 0
        formatted = ""

        if term[i] == "!":
            formatted += "not " + term[i + 1]
            i += 2
        else:
            formatted += term[i]
            i += 1

        while i < len(term):
            if term[i] == "!":
                formatted += " and not " + term[i + 1]
                i += 2
            else:
                formatted += " and " + term[i]
                i += 1

        formatted_terms.append(formatted)

    return " or ".join(formatted_terms)


TERMINATE = "END"

if __name__ == "__main__":

    bFunc = sys.argv[1]
    num_vars = int(sys.argv[2])
    formatted = parse_bfunc(bFunc)

    while True:
        bits = input()

        if bits == TERMINATE:
            break

        # with open("../utils/test.txt", "a+") as f:
        #     f.write(bits + "\n")

        converted = []
        for bit in bits:
            if bit == "1":
                converted.append(True)
            else:
                converted.append(False)

        if num_vars == 5:
            A, B, C, D, E = converted
        elif num_vars == 9:
            A, B, C, D, E, F, G, H, I = converted
        elif num_vars == 13:
            A, B, C, D, E, F, G, H, I, J, K, L, M = converted

        res = boolExpr.parseString(formatted)[0]
        print(bool(res))