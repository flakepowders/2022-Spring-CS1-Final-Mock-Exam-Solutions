# Automata
# 2022 Spring CS1 Final Mock Exam
# P02_satisfyme의 모범 답안입니다.
# CS1 수준에서의 모범 답안이므로, 최선의 해답이 아닐 수도 있습니다.
# 주석은 코드 이해를 돕기 위해 작성했고, 해설 목적은 아닙니다.
# 자세한 해설은 같이 첨부된 Editorial을 참고해 주세요.

def SatisfyExaminer(N):
    result = 0
    # N의 모든 소인수들의 합을 저장합니다.
    if N == 1:
       return 1
       # 만약 N이 1이라면, 1을 반환하고 종료합니다.
    for i in range(2, N+1):
        while N % i==0:
            N //= i
            result += i
        # 만약 N을 나누는 i를 발견한다면, N이 i로 나누어떨어지지 않을 때까지 계속해서 나눕니다.
        # N을 i로 나눌 때마다, 결과값에는 i를 더해 줍니다.
        # i가 합성수라면, 이미 지나오면서 N을 i의 소인수들로 각각 나눠 준 이후이므로 N을 합성수로 나누는 일은 없습니다.
    return result
