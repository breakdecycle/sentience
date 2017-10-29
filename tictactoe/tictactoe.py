from __future__ import print_function # Python 2/3 compatibility
import random
import itertools

# Define squares
def play():
	win = [
		set([1, 2, 3]),
		set([4, 5, 6]),
		set([7, 8, 9]),
		set([1, 5, 9]),
		set([1, 4, 7]),
		set([2, 5, 8]),
		set([3, 6, 9]),
		set([3, 5, 7])
	]
	options = list(range(1,10))
	p1 = []
	p2 = []
	state = []

	while len(options) > 0 or any(set(s).issubset(p1) for s in win) or any(set(s).issubset(p2) for s in win):

		x1 = random.choice(options)
		p1.append(x1)
		options.remove(x1)

		x2 = random.choice(options)
		p2.append(x2)
		options.remove(x2)

		 if any(set(s).issubset(p1) for s in win):
				iters = [iter(p1), iter(p2)]
				state = list(next(it) for it in itertools.cycle(iters))
				result = [state, 1]
				break

		elif any(set(s).issubset(p2) for s in win):
				iters = [iter(p1), iter(p2)]
				state = list(next(it) for it in itertools.cycle(iters))
				result = [state, 1]
				break

		else:
			iters = [iter(p1), iter(p2)]
			state = list(next(it) for it in itertools.cycle(iters))
			result = [state, 0]
			break

	return result


def main():
	sample = []
	x = 0
	while x < 1000:
		sample.append(play())
		x += 1
	print('Returning {} completed games...'.format(len(sample)))
	return [s for s in sample]


if __name__ == '__main__':
	main()
