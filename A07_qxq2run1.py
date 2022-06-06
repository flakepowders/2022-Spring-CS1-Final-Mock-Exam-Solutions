# Automata
# 2022 Spring CS1 Final Mock Exam
# P07_qxq2run1의 모범 답안입니다.
# CS1 수준에서의 모범 답안이므로, 최선의 해답이 아닐 수도 있습니다.
# 주석은 코드 이해를 돕기 위해 작성했고, 해설 목적은 아닙니다.
# 자세한 해설은 같이 첨부된 Editorial을 참고해 주세요.

def gcd(m, n):
    m, n = abs(m), abs(n)
    while n > 0:
        m, n = n, m % n
    return m
# 수업 시간에 다루었을 GCD 함수입니다.
# 사실 math라는 모듈에 내장되어 있어서 굳이 구현할 필요는 없습니다.

def QXQ2RUN1(a, b, c, d):
    if d < 0:
        c, d = -c , -d
    if b < 0:
        a, b = -a, -b
    # 각 분수의 분모를 양수로 맞춰 줍니다.

    g = gcd(c, d)
    c, d = c // g, d // g
    g = gcd(a, b)
    a, b = a // g, b // g
    # 각 분수를 약분해 줍니다.
    # 위 처리만 조심하면, 이제 조건 분기만 남았습니다.
    if a == 0:
        if c > 0:
            return 1
        if c == 0:
            return 2
        if c < 0:
            return "undefined"
    h = 1
    if a < 0 and c % 2 != 0:
        if d % 2 == 0:
            return "undefined"
        h = -1
    a, c = abs(a), abs(c)
    p = q = None
    for i in range(1,a+1):
        if i ** d == a:
            p = i
        if i ** d > a:
            break
    for i in range(1, b+1):
        if i ** d == b:
            q = i
        if i ** d > b:
            break
    if p == None or q == None:
        return "irrational"
    return abs(p ** c * h + q ** c) % 2 ** 32
