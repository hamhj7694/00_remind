# openai api 사용 가능한 모듈 설치
# pip install openai

from openai import OpenAI

# pip install dotenv
# dotenv() 사용해서 env 읽기 -- 외부 모듈 다운로드 필요 
from dotenv import load_dotenv
load_dotenv()

# OpenAI 객체 생성
client= OpenAI()
previous_id = None

print('AI 챗봇 시작 (종료:exit)')
while True:
    question= input('\n사용자: ')
    if question.lower() == 'exit':
        break

    # LLM AI 호출 및 응답
    response= client.responses.create(
        model='gpt-4o-mini',
        instructions="당신은 친절한 한국어 AI 챗봇입니다. 이름은 '펫펫'입니다. 당신은 애교가 많은 강아지라서 언제나 끝은 '멍멍!' 이라고 말합니다.",
        input=question,
        previous_response_id=previous_id
    )

    #응답결과 출력
    print('AI:', response.output_text)

    #이전 대화 기억
    previous_id= response.id