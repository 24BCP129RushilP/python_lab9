def create_tuple_list(end, current=1, result=None):

    if result is None:
        result = []
    
 
    if current > end:
        return result
    
    
    result.append((current, current**2, current**3))
    
    
    return create_tuple_list(end, current + 1, result)


end_value = 5
result = create_tuple_list(end_value)
print(f"List of tuples for x from 1 to :",end_value)
for tup in result:
    print(tup)