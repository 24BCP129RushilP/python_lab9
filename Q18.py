def average_list(lst, total=0, count=0):
    if not lst:
        return total / count if count > 0 else 0
    return average_list(lst[1:], total + lst[0], count + 1)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Average:", average_list(numbers))