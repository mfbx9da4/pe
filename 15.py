right = (1, 0)
down = (0, 1)

[0, 0, 0, 0]
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
[1, 1, 0, 0]
[1, 0, 1, 0]
[1, 0, 0, 1]
[0, 1, 1, 0]
[0, 1, 0, 1]
[0, 1, 1, 0]

dim = 4

from itertools import permutations
for i in range(dim+1):
    tmp = [1]*i + [0]*(dim-i); print '....', tmp, i
tmp = [1]*10 + [0]*10
tmp = [1]*3 + [0]*3
tmp = [1]*4 + [0]*4
S = set()
for x in permutations(tmp):
    print x
    S.add(x)

for i, a in zip(range(2, 5), (6, 20, 70)):
	print 'a*%d^4+b*%d^3+c*%d^2+d*%d^1+e=%d,' % (i, i, i, i, a),

for i, a in zip(range(1, 5), (2, 6, 20, 70)):
	print 'b*%d^3+c*%d^2+d*%d^1+e=%d,' % (i, i, i, a),

seq = [[0], [1]]
def perm(seq, targL, options):
	if not seq:
		seq = [ [i] for i in range(options)]
	print len(seq[0]), len(seq)
	if targL == len(seq[0]):
		return seq
	else:
		new = []
		for i in range(options):
			for x in seq:
				tmp = [i] + x
				# print i, tmp
				new.append(tmp)
		return perm(new, targL, options)
