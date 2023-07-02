#!/usr/bin/python3
import sys


def is_module_imported(module_name):
    return module_name in sys.modules

print(is_module_imported('math'))  # True
print(is_module_imported('random'))  # False
