# 단어어 해당 단어의 빈도수를 담은 리스트를 선언합니다. 수정하지 마세요.
pairs = [
    ('time', 8),
    ('the', 15),
    ('turbo', 1),
]

#(단어, 빈도수) 쌍으로 이루어진 튜플을 받아, 빈도수를 리턴합니다.    
def get_freq(pair):

    return pair[1]

#(단어, 빈도수) 꼴 튜플의 리스트를 받아, 빈도수가 낮은 순서대로 정렬하여 리턴합니다.
def sort_by_frequency(pairs):

    return sorted(pairs, key=get_freq)

print(sort_by_frequency(pairs))
