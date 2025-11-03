import random, sys

random.seed(0)
programs = list(range(974))
random.shuffle(programs)

n = int(sys.argv[1]) - 1

if n < 0:
    exit(1)

if n < len(programs):
    print(programs[n] + 1)
else:
    print("EOF")