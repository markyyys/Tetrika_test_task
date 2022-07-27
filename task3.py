def appearance(intervals):
    int_inter = []
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    lesson = intervals['lesson']
    for t in range(0, len(tutor) - 1, 2):
        for p in range(0, len(pupil) - 1, 2):
            if pupil[p] in range(tutor[t], tutor[t + 1]) or pupil[p + 1] in range(tutor[t], tutor[t + 1]) \
                    or tutor[t] in range(pupil[p], pupil[p + 1]) or tutor[t + 1] in range(pupil[p], pupil[p + 1]):
                if max(tutor[t], pupil[p]) >= lesson[0] and min(tutor[t + 1], pupil[p + 1]) <= lesson[1]:
                    int_inter.append(max(tutor[t], pupil[p]))
                    int_inter.append(min(tutor[t + 1], pupil[p + 1]))
                elif max(tutor[t], pupil[p]) < lesson[0]:
                    int_inter.append(lesson[0])
                    int_inter.append(min(tutor[t + 1], pupil[p + 1]))
                elif min(tutor[t + 1], pupil[p + 1]) > lesson[1]:
                    int_inter.append(max(tutor[t], pupil[p]))
                    int_inter.append(lesson[1])

    sum = 0
    for i in range(1, len(int_inter) - 1):
        if int_inter[i] < int_inter[i-1]:
            int_inter[i] = int_inter[i-1]
    for i in range(0, len(int_inter) - 1, 2):
        if int_inter[i + 1] - int_inter[i] > 0:
            sum += int_inter[i + 1] - int_inter[i]
    return sum


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
