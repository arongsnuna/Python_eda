# 트럼프 대통령의 트윗 모음을 불러옵니다.
from tweets import trump_tweets

# 그래프에 필요한 라이브러리를 불러옵니다. 
import matplotlib.pyplot as plt

# 단어구름에 필요한 라이브러리를 불러옵니다. 
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# 특화된 컨테이너 모듈에서 수 세기를 돕는 메소드를 불러옵니다.
from collections import Counter

# 문자열 모듈에서 특수문자를 처리를 돕는 메소드를 불러옵니다. 
from string import punctuation

# 엘리스에서 파일 송출에 필요한 패키지를 불러옵니다. 
from elice_utils import EliceUtils
elice_utils = EliceUtils()


# 데이터 전처리를 실행합니다. 
def preprocess_text(text):
    # 분석을 위해 text를 모두 소문자로 변환합니다.
    text = text.lower()
    
    # @와 #을 제외한 특수문자로 이루어진 문자열 symbols를 만듭니다.
    symbols = punctuation.replace('@', '').replace('#', '')
    
    # text에서 @와 #을 제외한 모든 특수문자를 제거합니다.
    for symbol in symbols:
        text = text.replace(symbol, '')
    
    # text를 띄어쓰기 단위로 쪼갭니다.
    words = text.split()
    return words
    

# 해시태그와 키워드를 추출합니다. 
def analyze_text(words):
    # 키워드, 해시태그, 멘션을 저장할 리스트를 각각 생성합니다.
    keywords, hashtags, mentions = [], [], []
    
    # 걸러낼 단어를 자유롭게 추가 or 삭제해보세요.
    filter_words = ['the', 'to', 'of', 'in', 'for', 'and', 'from', 'is', 'on', 'it', 'this', 'that', 'are', 'was', 'will', 'with', 'very', 'a', 'be', 'by', 'must', 'just', 'not']
    
    # 쪼갠 단어들을 분류합니다.
    for word in words:
        
        '''
        filter_words 를 이용해 의미없는 단어는 제거할 수 있습니다.
        아래 주석을 해제하여 일부 단어를 제거한 결과를 확인할 수 있습니다.
        '''
        # if word in filter_words :
        #     continue
        
        # 해시태그일 경우
        if word.startswith('#'):
            # 해시(#)를 제외한 단어를 plain_word 변수에 저장합니다.
            plain_word = word[1:]
            
            # plain_word를 적절한 리스트에 추가합니다.
            keywords.append(plain_word)
            hashtags.append(plain_word)
        
        # 멘션일 경우
        elif word.startswith('@'):
            # @ 기호를 제외한 단어를 plain_word 변수에 저장합니다.
            plain_word = word[1:]
            
            # plain_word를 적절한 리스트에 추가합니다.
            keywords.append(plain_word)
            mentions.append(plain_word)
        
        # 둘 다 아닐 경우
        else:
            # word를 적절한 리스트에 추가합니다.
            keywords.append(word)
    
    return keywords, hashtags, mentions


def filter_by_month(tweet_data, month):
    # month를 문자열로 바꾼 month_string을 선언합니다.
    # 이 때 한 자리 수는 앞에 '0'을 넣어줍니다. (ex: 1 => '01')
    month_string = '0' + str(month) if month < 10 else str(month)
    
    # 선택한 달의 트윗을 filtered_tweets에 저장합니다.
    filtered_tweets = []
    for date, tweet in tweet_data:
        # 트윗의 날짜가 선택한 달에 속해 있으면 트윗의 내용을 filtered_tweets에 추가합니다.
        if date.startswith(month_string):
            filtered_tweets.append(tweet)
    
    return filtered_tweets


# 트윗 통계를 출력합니다.
def show_stats():
    keyword_counter = Counter()
    hashtag_counter = Counter()
    mention_counter = Counter()
    
    for _, tweet in trump_tweets:
        keyward, hashtag, mention = analyze_text(preprocess_text(tweet))
        keyword_counter += Counter(keyward)
        hashtag_counter += Counter(hashtag)
        mention_counter += Counter(mention)
    
    # 가장 많이 등장한 키워드, 해시태그, 멘션을 출력합니다.
    top_ten = hashtag_counter.most_common(10)
    for hashtag, freq in top_ten:
        print('{}: {}회'.format(hashtag, freq))


# 월 별 트윗 개수를 보여주는 그래프를 출력합니다. 
def show_tweets_by_month():
    months = range(1, 13)
    num_tweets = [len(filter_by_month(trump_tweets, month)) for month in months]
    
    plt.bar(months, num_tweets, align='center')
    plt.xticks(months, months)
    
    plt.savefig('graph.png')
    elice_utils = EliceUtils()
    elice_utils.send_image('graph.png')


# wordcloud 패키지를 이용해 트럼프 대통령 실루엣 모양의 단어구름을 생성합니다.
def create_word_cloud():
    
    counter = Counter()
    for _, tweet in trump_tweets:
        keywords, _, _ = analyze_text(preprocess_text(tweet))
        counter += Counter(keywords)
    
    trump_mask = np.array(Image.open('trump.png'))
    cloud = WordCloud(background_color='white', mask=trump_mask)
    cloud.fit_words(counter)
    cloud.to_file('cloud.png')
    elice_utils.send_image('cloud.png')


# 입력값에 따라 출력할 결과를 선택합니다. 
def main(code=1):
    # 가장 많이 등장한 키워드, 해시태그, 멘션을 출력합니다.
    if code == 1:
        show_stats()
    
    # 트럼프 대통령의 월별 트윗 개수 그래프를 출력합니다.
    if code == 2:
        show_tweets_by_month()
    
    # 트럼프 대통령의 트윗 키워드로 단어구름을 그립니다.
    if code == 3:
        create_word_cloud()


# main 함수를 실행합니다. 
if __name__ == '__main__':
    main(3)
