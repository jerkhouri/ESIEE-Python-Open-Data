#!/usr/bin/python3
import csv

with open('data/data.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		print(', '.join(row))
