#!/usr/bin/env python3

import sys
import re
if len(sys.argv) == 3:
	arr = re.findall(sys.argv[1], sys.argv[2])
	if not arr:
		print("none")
	else:
		print(len(arr))
else:
	print("none")
