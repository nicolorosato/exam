#! /usr/bin/env python3

'''importing sys'''

import sys

'''
From module Capitals we import both the key and the value in order to make available the function.
'''

from capitals import check_capital, check_state

check_capital(sys.argv[1])
check_state(sys.argv[2])

