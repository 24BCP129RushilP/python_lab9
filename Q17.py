def sanitize_list(lst):
    if not lst:
        return []
    return [max(0, lst[0])] + sanitize_list(lst[1:])

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Sanitized list:", sanitize_list(numbers))