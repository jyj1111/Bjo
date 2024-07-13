def solution(str1, str2):
    s1 = ''.join(c.upper() for c in str1)
    s2 = ''.join(c.upper() for c in str2)

    S1 = [s1[i:i+2] for i in range(len(s1)-1) if s1[i:i+2].isalpha()]
    S2 = [s2[i:i+2] for i in range(len(s2)-1) if s2[i:i+2].isalpha()]

    n1 ,n2 ,n3 = len(S1), len(S2), 0
    for s in S1:
        if s in S2:
            S2.remove(s)
            n3 += 1

    if n1 == 0 and n2 == 0:
        return 65536
    else:
        return n3 * 65536 // (n1 + n2 - n3)
    
 