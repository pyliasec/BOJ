def max_sort(N, A, S) :
    for i in range(N) :
# # N : 배열 크기
# A : 배열 자체
# S : 최대 교환 횟수
# max_swap: 현재 인덱스에서 교환 가능한 최대 범위
## max_pos: 현재 범위 내에서 가장 큰 숫자의 인덱스
# i : 현재 인덱스ㅡㅡ





# 최대 범위        
        max_swap = min(N - 1, i + S)

# 수 찾기        
        max_pos = i
        for j in range(i + 1, max_swap + 1) :
            if A[j] > A[max_pos]:
                max_pos = j



#ㅗ
    #     for j in range(max_pos, i, -1) :
    #         A[j], A[j - 1] = A[j - 1], A[j]
    #         if S == 0 :
    #             return A
    # return A     

#ㅗㅗㅗㅗㅗㅗ
        # for j in range(max_pos, i, -1):
        #     A[j], A[j - 1] = A[j - 1], A[j]
        #     S -= 1




# 젤 큰 수 앞으로 전진~~        
        for j in range(max_pos, i, -1) :

            A[j], A[j - 1] = A[j - 1], A[j]
#           S = 0
            S -= 1
#           if S -= 1:
            if S == 0:
                return A
    return A


# help...


N = int(input())
A = list(map(int, input().split()))
S = int(input())

result = max_sort(N, A, S)
print(' '.join(map(str, result)))

# hhhhhhhhhhhhhhhhhhhhhh