# 코드가 너무 길다. 이건 어쩔 수 없을지도 다른사람 코드를 보면 %, enumerate를 썼다.
def solution(answers):
    students=[[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    good_stud = []
    score = [0, 0, 0]
    rep1, rep2, rep3 = 0, 0, 0
    # 답을 돌아가면서 비교하며 각 학생의 score 계산
    for i in range(len(answers)):
        if answers[i] == students[0][rep1]:
            score[0] += 1
        if answers[i] == students[1][rep2]:
            score[1] += 1
        if answers[i] == students[2][rep3]:
            score[2] += 1
        # rep 돌아가며 반복문을 넘으면 다시 0으로
        if rep1 == len(students[0])-1: rep1 = 0
        else: rep1 += 1
        if rep2 == len(students[1])-1: rep2 = 0
        else: rep2 += 1
        if rep3 == len(students[2])-1: rep3 = 0
        else: rep3 += 1
    # max 스코어를 가진 학생 답 출력에 넣기
    for j in range(3):
        if max(score) == score[j]:
            good_stud.append(j+1)
    return good_stud