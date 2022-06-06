# Automata
# 2022 Spring CS1 Final Mock Exam
# P04_skyscraper의 모범 답안입니다.
# CS1 수준에서의 모범 답안이므로, 최선의 해답이 아닐 수도 있습니다.
# 주석은 코드 이해를 돕기 위해 작성했고, 해설 목적은 아닙니다.
# 자세한 해설은 같이 첨부된 Editorial을 참고해 주세요.

def numberOfSkyscrapers(L):
    N = len(L)
    # 가로줄의 수를 저장합니다.
    M = len(L[0])
    # 세로줄의 수를 저장합니다.
    result = [0] * M
    # 결과값을 저장합니다. 결과값은 남쪽에서 보았을 때 세로줄마다 보이는 건물의 수이므로, 길이는 M입니다.
    for j in range(M):
        maxHeight = 0
        # 일단 그 줄에서 보이는 최대 높이를 0으로 설정합니다.
        for i in range(N-1, -1, -1):
            # 남쪽에서 북쪽 방향으로, 건물들을 하나씩 검사합니다.
            if L[i][j] > maxHeight:
                # 만약 이 건물이 그 줄에서 보이는 최대 높이보다 높다면,
                maxHeight = L[i][j]
                # 그 줄에서 보이는 최대 높이는 그 건물의 높이로 갱신해줍니다.
                result[j] += 1
                # 그 줄에서 보이는 건물의 개수도 1만큼 늘려 줍니다.
    return result
    