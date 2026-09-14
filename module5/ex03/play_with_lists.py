#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = []
print(arr)
for i in range(len(arr)):
	if arr[i] > 5:
		arr2.append(arr[i] + 2)
print(set(arr2))
