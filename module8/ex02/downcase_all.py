#!/usr/bin/env python3

import sys

def downcase_it(str):
	return str.lower()

if len(sys.argv) >= 2:
	i = 1
	while i <= len(sys.argv) - 1:
		print(downcase_it(sys.argv[i]))
		i += 1
else:
	print("none")
