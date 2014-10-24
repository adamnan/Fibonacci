#!/usr/bin/env python

nums = [1, 1]
print(1)
print(1)

for i in range(2, 100):
	nextFib = nums[-1] + nums[-2]
	nums.append(nextFib)
	print(nextFib)