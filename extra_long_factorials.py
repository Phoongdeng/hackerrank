#!/bin/python3

import sys

def extraLongFactorials(n):
    # Complete this function
    if n == 1:
    	return 1

    return n * extraLongFactorials(n-1)


def extraLongFactorials_2(n):
    # Complete this function
	d = [1]

	for i in range(2, n+1):

		for j in range(len(d)):
			d[j] *= i

		for j in range(len(d)):
			if d[j] < 10:
				continue

			if j == len(d)-1:
				d.append(0)

			d[j+1] += (d[j] // 10)
			d[j] %= 10

	for i in d[::-1]:
		print(i, end="")

if __name__ == "__main__":
	n = int(input().strip())
	extraLongFactorials_2(n)
