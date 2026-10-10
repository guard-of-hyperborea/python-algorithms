def analyze(numbers):
    res = {}
    d = {}
    
    res["unique"] = len(set(numbers))
    res["max"] = max(numbers)
    res["min"] = min(numbers)
    
    for num in numbers:
        d[num] = d.get(num , 0) + 1
    d_sorted = dict(sorted(d.items() , key = lambda x : x[1] , reverse = True))
    keys = list(d_sorted.keys())
    res["most_common"] = keys[0]
    return res

numbers = [4, 2, 7, 2, 9, 4, 1, 7, 5]
print(analyze(numbers))