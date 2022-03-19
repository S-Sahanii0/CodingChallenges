def closestNumbers(numbers):
    cache = {}
    
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if(i != j):
                diff = abs(numbers[i] - numbers[j])
                if diff in cache:
                    cache[diff].append((numbers[i], numbers[j]))
                else:
                    cache[diff] = [(numbers[i], numbers[j])]
    diff_list = list(cache.keys())
    
    for k,v in cache.items():
        if min(diff_list) == k:
            [print(*i) for i in sorted(v)]
            
closestNumbers([4,1,2,3])