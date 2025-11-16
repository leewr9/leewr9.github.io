---
title: Chain Component
category: LangChain
tag: [Chain, LangChain]
---

> LangChain의 핵심 컴포넌트 중 하나인 체인은 여러 LLM 호출, 프롬프트, 도구 사용 등을 순차적으로 연결해 하나의 파이프라인처럼 처리하는 구조입니다. 복잡한 워크플로우를 간단하게 구성할 수 있어, 다양한 AI 애플리케이션 개발에 필수적인 요소입니다.

---

## Chain

`Chain`은 여러 LLM, 프롬프트, 도구, 메모리 등 다양한 컴포넌트를 순차적으로 연결해 복잡한 작업을 자동화하는 핵심 구조입니다. 단일 LLM 호출을 넘어서, `입력 → 처리 → 출력`의 파이프라인을 자유롭게 설계할 수 있습니다.

- **프롬프트 체이닝**: 여러 프롬프트/LLM을 연결해 단계별로 처리
- **도구/메모리 연동**: 외부 API, 메모리 등과 결합해 동적 워크플로우 구현
- **복잡한 로직**: 조건 분기, 반복, 결과 조합 등 다양한 로직 구현 가능

### Structure

- `PromptTemplate`: 입력을 LLM이 이해할 수 있는 형태로 변환
- `LLM`: 실제 언어 모델 (`OpenAI`, `HuggingFace` 등)
- `OutputParser`: LLM의 출력을 원하는 형태로 가공

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("{question}에 대해 1문장으로 대답해줘")
llm = OpenAI()
parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"question": "LangChain이 뭐야?"})
print(result)
```

```bash
LangChain은 언어간의 커뮤니케이션을 쉽게 할 수 있도록 도와주는 플랫폼이다.
```

### RunnableLambda

`RunnableLambda`를 활용하면, 복잡한 워크플로우를 하나의 함수로 정의하고 `Chain`에 통합할 수 있습니다. 여러 체인 조합, 조건 분기, 반복 등 다양한 로직을 자유롭게 구현할 수 있습니다.

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# 요약
summary_prompt = PromptTemplate.from_template("질문을 한 문장으로 요약해줘: {question}")
llm = ChatOpenAI()
parser = StrOutputParser()
summary_chain = summary_prompt | llm |parser

# 답변
answer_prompt = PromptTemplate.from_template("{summary}에 대해 1문장으로 답변해줘")
answer_chain = answer_prompt | llm | parser

def workflow(inputs):
  summary = summary_chain.invoke({"question": inputs["question"]})
  print("Summary:", summary)
  answer = answer_chain.invoke({"summary": summary})
  print("Answer:", answer)
  return answer

chain = RunnableLambda(workflow)
chain.invoke({"question": "LangChain의 Chain 구조를 설명해줘. 다양한 체인 조합 방법도 서술형으로 함께 알려줘."})
```

```bash
Summary: LangChain의 Chain 구조 및 다양한 체인 조합 방법을 설명해주세요.
Answer: LangChain은 여러 개의 체인을 연결하여 원하는 형태의  구조를 생성할 수 있는 유연한 방식으로 다양한 체인 조합이 가능하며, 이를 통해 사용자는 다양한 언어 및 문화체계를 학습할 수 있습니다.
```

---

## Memory Chain

`Memory`를 `Chain`에 연결하면, 대화 이력이나 상태 정보를 활용한 AI 파이프라인을 만들 수 있습니다. `ConversationBufferMemory` 등 메모리 컴포넌트를 Chain에 통합하여, 이전 대화 내용을 기반으로 더 일관성 있는 응답을 생성할 수 있습니다.

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.memory import ConversationBufferMemory

prompt = PromptTemplate.from_template(
    "아래는 지금까지의 대화 이력입니다.\n{history}\n\nQ: {question}\nA:"
)
llm = OpenAI()
parser = StrOutputParser()
memory = ConversationBufferMemory()

chain = (prompt | llm | parser).with_config(memory=memory)


for q in ["안녕", "오늘 날씨 어때?", "내일은?"]:
    variables = memory.load_memory_variables({})
    result = chain.invoke({"question": q, "history": variables.get("history", "")})
    print(q, "=>", result)
    memory.save_context({"input": q}, {"output": result})
```

```bash
안녕 =>  안녕하세요? 저는 인공지능 비서입니다.
오늘 날씨 어때? =>  오늘은 대체로 맑은 날씨가 예상됩니다. 하 지만 춥지는 않아요.
내일은? =>  내일은 비가 올 확률이 높아요. 우산을 챙기는 것을 추천해요.
```

---

## Tool Chain

`Tool`을 `Chain`에 연결하면 외부 함수, API, 계산기 등 다양한 기능을 LLM 워크플로우에 통합할 수 있습니다. 작업 지시를 분석해 적절한 도구를 호출하는 등, 동적인 작업 수행이 가능합니다.

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai.llms import OpenAI
from langchain_community.tools import Tool

def get_birthday(_input=None) -> str:
    print("생일 도구를 호출합니다.")
    return "제 생일은 7월 20일입니다."

time_tool = Tool(
    name="GetBirthday",
    func=get_birthday,
    description="생일을 반환합니다."
)

prompt = PromptTemplate.from_template("생일이 언제야?")
llm = OpenAI()

chain = prompt | llm | time_tool

result = chain.invoke({})
print("생일 =>", result)
```

```bash
생일 도구를 호출합니다.
생일 => 제 생일은 7월 20일입니다.
```

---

## Reference

- [LangChain 공식 문서](https://docs.langchain.com/)

<nav class="post-toc" markdown="1">
  <h2>Table of Contents</h2>
* TOC
{:toc}
</nav>
