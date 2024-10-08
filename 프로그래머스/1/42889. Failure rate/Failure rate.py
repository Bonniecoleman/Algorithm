def solution(N, stages):
    # 스테이지별 도전자 수를 구함
    challenger = [0] * (N + 2)
    print('challenger init:', challenger)
    for stage in stages:
        challenger[stage] += 1
    print('challenger after:', challenger)

    # 스테이지별 실패한 사용자 수 계산
    fails = {} # 실패율
    total = len(stages) # 총 사용자의 수 

    # 각 스테이지를 순회하며, 실패율 계산

    for i in range(1, N+1):
        if challenger[i] == 0: # 도전한 사람이 없는 경우, 실패율은 0
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total # 실패율 구함
            total -= challenger[i] # 다음 스테이지 실패율을 구하기 위해 현재 스테이지의 인원을 뺌

    # 실패율이 높은 스테이지부터 내림차순으로 정렬

    result = sorted(fails, key = lambda x: fails[x], reverse = True)
    
    return result