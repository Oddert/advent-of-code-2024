import math as maths # I'll fight any american in a car park

from typing import List


def most_common_item(arr: list):
    '''
    For a given array of items, finds the item which occurs the more frequently.

    returns [any, int]: A tuple of the item and its count.
    '''
    count = {}
    top_item = [arr[0], 1]
    highest_value = arr[0]
    all_zeros = True
    for item in arr:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for item in count:
        if count[item] > top_item[1]:
            all_zeros = False
            top_item = [item, count[item]]
        if item > highest_value:
            highest_value = item
    return [highest_value, 1] if all_zeros else top_item


def prime_factors(number: int):
    '''
    Generic implementation of a function to find prime factors of a given number.

    Copied from example at https://www.geeksforgeeks.org/prime-factor/
    '''
    factors = []

    # If number is divisible by 2, find the number of times 2 can be factored in.
    while number % 2 == 0:
        factors.append(2)
        number = number / 2

    # 1 is skipped, number is now odd so 2 is skipped.
    # Loop over multiples of 2 up to the square root.
    for i in range(3, int(maths.sqrt(number)) + 1, 2):
        # For each value, attempt to divide number by idx.
        while number % i == 0:
            factors.append(i)
            number = number / i

    # Anything remaining is added as the last multiple. 
    if number > 2:
        factors.append(int(number))

    return factors


def lowest_common_multiple(*numbers):
    factor_list = []
    for number in numbers:
        primes = prime_factors(number)
        highest_factor_count = most_common_item(primes)
        highest_factor = maths.pow(*highest_factor_count)
        factor_list = [*factor_list, highest_factor]
    total = 1
    for factor in factor_list:
        total *= factor
    return total


def quicksort(items: List[int], start = None, end = None):
	if start is None:
		start = 0

	if end is None:
		end = len(items) - 1

	def partition(start, end):
		pivot_value = items[end]
		index = start - 1

		for j in range(start, end):
			if items[j] <= pivot_value:
				index += 1
				items[index], items[j] = items[j], items[index]

		index += 1
		items[index], items[end] = items[end], items[index]
		return index

	if start >= end:
		return
	
	pivot = partition(start, end)
	quicksort(items, start, pivot - 1)
	quicksort(items, pivot + 1, end)

	return items
