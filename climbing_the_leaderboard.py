#!/bin/python3

import os
import sys

#
# Complete the climbingLeaderboard function below.
#
def climbingLeaderboard(scores, alice):

# 1st Try : fail, Time out.
	# scores_set = []
	# for score in scores:
	# 	if score in scores_set:
	# 		continue
	# 	scores_set.append(score)

	# alice_rank = []

	# for a_score in alice:
	# 	rank = len(scores_set) + 1
	# 	for idx, score in enumerate(scores_set):
	# 		if a_score >= score:
	# 			rank = idx + 1
	# 			break
	# 	alice_rank.append(rank)

	# return alice_rank

# 2nd Try
	ranklist = list(set(scores))
	ranklist.sort(reverse = True)

	alice_rank = []

	for score in alice:

		top = len(ranklist)-1
		bot = 0

		if score < ranklist[top]:
			alice_rank.append(len(ranklist)+1)
			continue
		elif score >= ranklist[bot]:
			alice_rank.append(1)
			continue

		while bot < top:
			idx = ((top+bot)//2)

			if bot+1 == top:
				alice_rank.append(top+1)			
				break
			elif score == ranklist[idx]:
				alice_rank.append(idx+1)
				break
			elif score < ranklist[idx]:
				bot = idx
			else:
				top = idx

	return alice_rank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
