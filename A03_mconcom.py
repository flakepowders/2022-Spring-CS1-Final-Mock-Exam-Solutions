# Automata
# 2022 Spring CS1 Final Mock Exam
# P03_mconcom의 모범 답안입니다.
# CS1 수준에서의 모범 답안이므로, 최선의 해답이 아닐 수도 있습니다.
# 주석은 코드 이해를 돕기 위해 작성했고, 해설 목적은 아닙니다.
# 자세한 해설은 같이 첨부된 Editorial을 참고해 주세요.

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+2):
        if n % i == 0:
            return False
    return True
# 수업 시간에 자세히 다루었을 소수 판별 함수입니다.
    
def maxConsecutiveComposite(n):
    conscount = 0
    # 현재 몇 번 연속으로 합성수가 나오는 중인지를 저장합니다.
    result = 0
    # conscount의 최대값, 즉 결과값을 저장합니다.
    for i in range(2, n+1):
        # 2부터 N까지 모든 수를 검사합니다.
        if isPrime(i):
            conscount = 0
            # 만약 i가 소수라면, 합성수가 끊긴 것이므로 conscount를 초기화합니다.
            # i가 1인 경우는 아예 검사하지 않으므로 신경 쓰지 않아도 됩니다.
        else:
            conscount += 1
            # 만약 i가 합성수라면, 합성수가 이어진 것이므로 conscount에 1을 더합니다.
        if result < conscount:
            result = conscount
            # 결과값은 conscount의 최대값이어야 합니다.
            # 즉, conscount가 result보다 크다면, result를 conscount로 갱신해 줍니다.
    return result
    