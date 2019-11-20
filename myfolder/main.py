#! /usr/bin/env python3

import sys '''Importing sys module '''

'''
From module Capitals we import both the key,

the value in order to make available the function.
'''

from capitals import check_capital, check_state

'''Allow user to input from the terminal,

2 arguments.
'''

check_capital(sys.argv[1])
check_state(sys.argv[2])
