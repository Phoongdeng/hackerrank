#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
	result = len(a)
	temp = {}

	for idx, val in enumerate(a):
		if val in temp:
			distance = idx - temp.get(val)
			if distance == 1:
				return 1

			result = min(result, distance)

		temp[val] = idx

	if len(a) == result:
		result = -1

	return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
