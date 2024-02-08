import random
import time

def get_me_random_list(n):
    """Generate a list of n elements in random order."""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    return sorted(a_list)

def time_sort(sort_func, data):
    start = time.time()
    sort_func(data)
    end = time.time()
    return end - start

if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        # Python Sort
        total_time = sum(time_sort(python_sort, get_me_random_list(the_size)) for _ in range(100)) / 100
        print(f"Python sort took {total_time:10.7f} seconds to run, on average for a list of {the_size} elements.")

        # Insertion Sort
        total_time = sum(time_sort(insertion_sort, get_me_random_list(the_size)) for _ in range(100)) / 100
        print(f"Insertion sort took {total_time:10.7f} seconds to run, on average for a list of {the_size} elements.")

        # Shell Sort
        total_time = sum(time_sort(shell_sort, get_me_random_list(the_size)) for _ in range(100)) / 100
        print(f"Shell sort took {total_time:10.7f} seconds to run, on average for a list of {the_size} elements.")
