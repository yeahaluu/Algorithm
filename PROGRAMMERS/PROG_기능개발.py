import math

def solution(progresses, speeds):
	# stack에 계산한 값을 넣어놓는다
    stack = []
    for i in range(len(progresses)):
        stack.append(math.ceil((100 - progresses[i])/speeds[i]))
	# 첫 숫자부터 자기보다 큰 숫자가 있으면 그 전까지 배포 (세여진 숫자 answer리스트에 넣기)
    max_num = stack[0]
    count_num = 1
    answer = []
    for j in range(1, len(stack)):
        if max_num < stack[j]:
            max_num = stack[j]  # 이 부분을 놓쳐서 잠시 헤맸음ㅠ 이런건 실수하지 말자
            answer.append(count_num)
            count_num = 0
        count_num += 1
    answer.append(count_num)
    return answer