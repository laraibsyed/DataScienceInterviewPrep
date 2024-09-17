def duplicates(input):
    dup = []
    count = {}

    for num in input:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num, i in count.items():
        if i > 1:
            dup.append(num)
    
    return dup
input = [1,2,3,1,3,6,5]
results = duplicates(input)
print(results)