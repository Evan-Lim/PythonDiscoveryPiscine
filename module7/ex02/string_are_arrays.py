#!/usr/bin/env python3

import sys
if len(sys.argv) == 2:
	i = 0
	z = 0
	while i < len(sys.argv[1]) - 1:
		if sys.argv[1][i] == 'z':
			z += 1
		i += 1
	if not z:
		print("none")
	else:
		while z > 0:
			print("z", end="")
			z -= 1
		print()
else:
	print("none")
