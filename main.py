"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	pass

def test_simple_work():
	""" done. """
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(8, 3, 2) == 1  #TODO: fix
	assert simple_work_calc(9, 2, 3) == 1  #TODO: fix

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	pass

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	pass

def test_work():
	""" done. """
	assert work_calc(8, 2, 2,lambda n: n) == 32 
	assert work_calc(8, 1, 2, lambda n: n*n) == 1 # TODO: fix
	assert work_calc(8, 3, 2, lambda n: 1) == 1   # TODO: fix

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Params:
	work_fn1....a curried version of work_calc expecting a single input n
	work_fn2....a curried version of work_calc expecting a single input n
	sizes.......list of values for n to compare these two work functions.

	Returns:
	A list of tuples of the form
	[(n, work_fn1(n), work_fn2(n)), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_work_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def print_span_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'S_1', 'S_2'],
							floatfmt=".3f",
							tablefmt="github"))
def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	
	res = compare_work(work_fn1, work_fn2)
	print_work_results(res)

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different span recurrences for 
	given input sizes.

	Params:
	span_fn1....a curried version of span_calc expecting a single input n
	span_fn2....a curried version of span_calc expecting a single input n
	sizes.......list of values for n to compare these two span functions.

	Returns:
	A list of tuples of the form
	[(n, span_fn1(n), span_fn2(n)), ...]
	
	"""
	result = []
	for n in sizes:
		# compute S(n) using current a, b, f
		result.append((
			n,
			span_fn1,
			span_fn2
			))
	return result

def test_compare_span():
	assert span_calc(10, 2, 2, lambda n: 1) == 1    # TODO: fix
	assert span_calc(20, 1, 4, lambda n: n*n) == 1  #TODO: fix
	assert span_calc(30, 3, 4, lambda n: n) == 1    #TODO: fix

	## make span_fn1 and span_fn2
	res = compare_span(span_fn1, span_fn2)
	print_span_results(res)
