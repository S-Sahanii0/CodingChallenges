def solution(S, C):
    lines = S.split('\n')
    values = []
    header = lines[0].split(",")
    header_index = header.index(C)

    for lines in lines[1:]:
        data = lines.split(",")
        values.append(data[header_index])
    print(max(values))
    return max(values)

    
solution("id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7", "age")
