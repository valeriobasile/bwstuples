#!/usr/bin/env python3

import sys
from math import floor, gcd

tsvfile = sys.argv[1]

instances = []
with open(tsvfile) as f:
	for line in f:
		id, text = line.strip().split("\t")
		instances.append({"id": id, "text": text})

n = len(instances)
k = eval(sys.argv[2])
p = eval(sys.argv[3])

while gcd(n, k) != 1:
	instances = instances[:-1]
	n = len(instances)

tuples = []
for j in range(p):
	for x in range(int(floor(n/k))):
		t = [(x*(k**(j+1)) + (i*(k**j))) % n for i in range(k)]
		tuples.append(t)
		
for t in tuples:
	#print ("\t".join([str(w) for w in t]))
	for i in t:
		print ("{0}\t{1}".format(instances[i]["id"], instances[i]["text"]))
	print ()
