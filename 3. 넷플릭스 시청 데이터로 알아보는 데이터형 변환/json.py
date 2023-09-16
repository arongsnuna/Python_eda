# JSON (JavaScript Object Notation)
## {key: value}
- 웹 환경에서 데이터를 주고 받는 가장 표준적인 방식
- 키를 이용하여 원하는 데이터만 빠르게 추출 가능
- 데이터가 쉽게 오염되지 않음
- 다른 포맷에 비해 용량이 조금 큰 편

![%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202023-09-17%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.56.56.png](attachment:%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202023-09-17%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.56.56.png)



# json 패키지를 임포트합니다.
import json



#JSON 파일을 읽고 문자열을 딕셔너리로 변환합니다.
def create_dict(filename):
    with open(filename) as file:
        json_string = file.read()
        
        return json.loads(json_string)



#JSON 파일을 읽고 딕셔너리를 JSON 형태의 문자열로 변환합니다.
def create_json(dictionary, filename):
    with open(filename, 'w') as file:
        # 함수를 완성하세요.
        json_string = json.dumps(dictionary)
        file.write(json_string)
        
        
        
# 아래 주석을 해제하고 결과를 확인해보세요.  
src = 'netflix.json'
dst = 'new_netflix.json'

netflix_dict = create_dict(src)
print('원래 데이터: ' + str(netflix_dict))

netflix_dict['Dark Knight'] = 39217
create_json(netflix_dict, dst)
updated_dict = create_dict(dst)
print('수정된 데이터: ' + str(updated_dict))
