def parallel(a, b, c, d) :
    g1 = (a[1] - b[1]) / (a[0] - b[0])
    g2 = (c[1] - d[1]) / (c[0] - d[0])
    
    if g1 == g2 :
        return 1 
    else : return 0 

def solution(dots):
    
    res1 = parallel(dots[0], dots[1], dots[2], dots[3])
    res2 = parallel(dots[0], dots[2], dots[1], dots[3])
    res3 = parallel(dots[0], dots[3], dots[1], dots[2])
    
    if 1 in ([res1, res2, res3]) :
        return 1 
    else : return 0