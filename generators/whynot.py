# biologists?
#
# python isn't very good at numerical computing

from random import randrange
from itertools import islice, tee

nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
windowed_averages = lambda g, n=2: (sum(xs)/len(xs) for xs in nwise(g, n))

from timeit import Timer

print(Timer('''
(xs[:-1] + xs[1:] / 2)
''', setup='''
from numpy.random import randint
xs = randint(0, 10, size=1_000_000)
''').timeit(number=5))

# >>> 0.02231427100196015

# large scales python has easy memory use but terrible numerical computing
# just use numpy
# python has terrible numerical support

print(Timer('''
list(windowed_average(xs, 2))
''', setup='''
from itertools import islice, tee
from random import randrange
nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
windowed_average = lambda g, n=2: (sum(xs)/len(xs) for xs in nwise(g, n))
xs = [randrange(0, 10) for _ in range(1_000_000)]
''').timeit(number=5))

# >>> 1.5014756259915885