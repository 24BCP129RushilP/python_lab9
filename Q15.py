def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])


numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Reversed list:", reverse_list(numbers))