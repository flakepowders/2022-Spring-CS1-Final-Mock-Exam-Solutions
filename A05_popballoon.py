# Automata
# 2022 Spring CS1 Final Mock Exam
# P05_popballoon의 모범 답안입니다.
# CS1 수준에서의 모범 답안이므로, 최선의 해답이 아닐 수도 있습니다.
# 주석은 코드 이해를 돕기 위해 작성했고, 해설 목적은 아닙니다.
# 자세한 해설은 같이 첨부된 Editorial을 참고해 주세요.

def popballoon(L):
    N, M = len(L), len(L[0])
    balloon = 0
    # 남은 풍선의 개수를 저장합니다.
    for i in range(N):
        for j in range(M):
            if L[i][j] == 1:
                balloon += 1
                # 처음 풍선의 개수를 세 줍니다.
    result = 0
    # 시행 횟수를 저장해 놓는 변수입니다.
    while balloon > 0:
        # 남은 풍선의 개수가 0개 이상이라면, 시행을 이어갑니다.
        result += 1
        if result % 2 == 1:
            # 홀수 번째 시행에서는 동쪽에서 서쪽으로 풍선을 터트립니다.
            for i in range(N):
                for j in range(M-1, -1, -1):
                    if L[i][j] == 1:
                        balloon -= 1
                        L[i][j] = 0
                        break
                        # 각 행에 대해 풍선을 처음으로 찾았다면, 그 풍선을 제거하고 남은 풍선의 수를 1 빼줍니다.
                        # 더 이상 터트리면 안 되므로 break문을 통해 루프를 빠져나갑니다.
        else:
            # 짝수 번째 시행에서는 남쪽에서 북쪽으로 풍선을 터트립니다.
            # 이것을 제외하면 구현 알고리즘은 홀수 번째 시행과 완전히 같습니다.
            for j in range(M):
                for i in range(N-1, -1, -1):
                    if L[i][j] == 1:
                        balloon -= 1
                        L[i][j] = 0
                        break
    return result