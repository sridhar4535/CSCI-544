import sys
import os
import time
from itertools import izip
from collections import Counter


def numDups(a, b):
    if len(a) > len(b):
        (a, b) = (b, a)

    a_count = Counter(a)
    b_count = Counter(b)

    return sum(min(b_count[ak], av) for (ak, av) in a_count.iteritems())


start_time = time.time()

fn1 = sys.argv[1]
fn2 = sys.argv[2]

if os.path.exists(fn1) and os.path.exists(fn2):
    fr1 = open(fn1, 'r')
    fr2 = open(fn2, 'r')
    correct = 0
    incorrect = 0

    with open(fn1) as textfile1:
        with open(fn2) as textfile2:
            for (x, y) in izip(textfile1, textfile2):
                x = x.strip()
                y = y.strip()
                a = x.split()
                b = y.split()
                matching = numDups(a, b)
                correct = correct + matching
                incorrect = incorrect + len(a) - matching

    print correct
    print incorrect
    print correct + incorrect
    print 1.0 * correct / (correct + incorrect)
else:

    print 'File does not exists'

print '--- %s seconds ---' % (time.time() - start_time)