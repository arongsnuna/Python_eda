def preprocess_text(text):
    # 분석을 위해 text를 모두 소문자로 변환합니다.
    text = text.lower()
    
    # @와 #을 제외한 특수문자로 이루어진 문자열 symbols를 만듭니다.
    symbols = punctuation.replace('@', '').replace('#', '')

    for punc in symbols:
      text = text.replace(punc,'')
    
    return text.split()
    