def solution(lines):
    max_val = max(max(line) for line in lines)
    min_val = min(min(line) for line in lines)
    
    n = max_val - min_val + 1
    cnt = 0

    res_line = [0] * n
    
    for line in lines :
        for i in range(line[0], line[1]) :
            res_line[i - min_val] += 1
            
    for a in res_line : 
        if a >= 2 :
            cnt += 1
    
    return cnt