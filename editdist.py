

import sys


def find_dist(first, second, len1, len2):
	if len1 == 0:
		return len2
	if len2 == 0:
		return len1
	if first[len1-1] == second[len2-1]:
		return find_dist(first,second, len1-1, len2-1)
	return 1 + min(find_dist(first, second, len1-1, len2), find_dist(first, second, len1, len2-1), find_dist(first, second, len1-1, len2-1))

	



if __name__ == "__main__":
	lines = [line for line in sys.argv]
	str1 = lines[1]
	str2 = lines[2]
	print(find_dist(str1, str2, len(str1), len(str2)))


import csv
with open('csvfile.csv', "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)