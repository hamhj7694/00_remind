# 모듈 설치
# pip install -U langchain-core langchain-openai langchain-google-genai

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI # 모델

from langchain_core.prompts import ChatPromptTemplate # 프롬프트 모양
from langchain_core.output_parsers import StrOutputParser # 아웃풋

#1. 사용할 모델 선택
# llm= ChatOpenAI(model='gpt-4o-mini')
llm= ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')

#2. 프롬프트 생성
prompt= ChatPromptTemplate.from_messages([
    ('system', '너는 상냥 여고생이야. 상냥하고 귀엽지만 짧게 대답해줘.'),
    ('human', '{question}')
])

#3. 체인 구성하기 -- LCEL 랭체인 표현 언어
chain = prompt | llm | StrOutputParser() # | 는 파이프 연산자.. 구성 요소를 체인처럼 연결

#4. 챗봇 실행
print('챗봇 시작')
while True:
    question= input('\n 나: ')
    if question.lower() == 'exit':
        break

    answer = chain.invoke({'question':question})
    print('AI:', answer)