import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order."""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    for element in a_list:
        if element == item:
            return True
    return False

def ordered_sequential_search(a_list, item):
    for element in a_list:
        if element == item:
            return True
        elif element > item:
            return False
    return False

def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

def main():
    list_sizes = [500, 1000, 5000]
    for size in list_sizes:
        print(f"\nTesting list size: {size}")

        # Sequential Search
        total_time_sequential = sum(time_search(sequential_search, get_me_random_list(size), -1) for _ in range(100)) / 100
        print(f"Sequential Search took {total_time_sequential:.7f} seconds to run, on average for a list of {size} elements.")

        # Ordered Sequential Search
        total_time_ordered = sum(time_search(ordered_sequential_search, sorted(get_me_random_list(size)), -1) for _ in range(100)) / 100
        print(f"Ordered Sequential Search took {total_time_ordered:.7f} seconds to run, on average for a list of {size} elements.")

        # Binary Search Iterative
        total_time_binary_iter = sum(time_search(binary_search_iterative, sorted(get_me_random_list(size)), -1) for _ in range(100)) / 100
        print(f"Binary Search Iterative took {total_time_binary_iter:.7f} seconds to run, on average for a list of {size} elements.")

        # Binary Search Recursive
        total_time_binary_recur = sum(time_search(binary_search_recursive, sorted(get_me_random_list(size)), -1) for _ in range(100)) / 100
        print(f"Binary Search Recursive took {total_time_binary_recur:.7f} seconds to run, on average for a list of {size} elements.")

def time_search(search_func, data, target):
    start = time.time()
    search_func(data, target)
    end = time.time()
    return end - start

if __name__ == "__main__":
    main()
