def solution(babbling):
    cnt = 0
    can_speak = ['aya', 'ye', 'woo', 'ma']
    for word in babbling :
        for s in can_speak :
            if word.find(s) !=  -1 :
                word = word.replace(s, "1")
        word = word.replace("1", "")
        if len(word) == 0 :
            cnt += 1
            
    return cnt
                