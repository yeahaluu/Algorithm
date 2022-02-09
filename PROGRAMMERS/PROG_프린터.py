# 문제처럼 [0]의 인쇄물을 확인하고 뒤로 넘기면 내가 궁금한 인쇄물의 위치가 계속 바뀐다.
# 그래서 pointer를 이용.

def solution(priorities, location):
    counter = 0
    pointer = 0
    while priorities[location] != 0:
        if priorities[pointer] == max(priorities):
            priorities[pointer] = 0
            counter += 1
        if pointer < len(priorities)-1:
            pointer += 1
        else:
            pointer = 0
    return counter