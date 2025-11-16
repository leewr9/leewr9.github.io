---
title: Agent Architecture
category: LangChain
tag: [Retriever, Memory, Tool, Chain, LangChain]
---

> LangChain은 대형 언어 모델 기반 애플리케이션을 쉽고 유연하게 개발할 수 있도록 다양한 컴포넌트와 아키텍처 패턴을 제공하는 오픈소스 프레임워크입니다. LLM을 활용한 챗봇, AI 에이전트, 문서 검색, 자동화 등 다양한 AI 서비스 개발을 위한 핵심 컴포넌트와 아키텍처를 제공합니다.

---

## Architecture

`LangChain`은 LLM, 프롬프트, 체인, 도구, 메모리, 검색기 등 다양한 컴포넌트로 구성되어 있습니다. 이들 컴포넌트를 조합하여 복잡한 AI 애플리케이션을 쉽게 구축할 수 있습니다.

[![](\assets\posts\2025-11-02-Agent Architecture.md\architecture.png)](\assets\posts\2025-11-02-Agent Architecture.md\architecture.png)

### Chain

`Chain`은 여러 LLM 호출, 프롬프트, 도구 사용 등을 순차적으로 연결해 하나의 파이프라인처럼 처리하는 구조입니다. 연결된 컴포넌트들은 입력을 받아 순차적으로 처리하며, 복잡한 워크플로우를 간단하게 구성할 수 있습니다.

```python
from langchain_openai.llms import OpenAI
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{question}에 대해 설명해줘")
llm = OpenAI()
chain = prompt | llm
result = chain.invoke({"question": "LangChain이란?"})
print(result)
```

```bash
LangChain은 언어 연쇄의 의미로, 언어 간 상호 작용 및 영향을  나타내는 개념입니다. 예를 들어, 어떤 언어가 다른 언어로부터  영향을 받아서 변화하게 되는 경우, 그 언어는 언어 연쇄의 일부 가 됩니다. 이와 같이 언어는 서로 영향을 주고 받으며 발전하고, 이러한 연쇄는 언어가 어떻게 변화하고 발전하는지를 이해하는  데 도움을 줍니다. 또한 언어 연쇄는 언어 간의 유사성이나 차이 를 파악하는 데에도 활용될 수 있습니다.
```

### Tool

`Tool`은 LLM이 사용할 수 있는 외부 기능(함수, API 등)을 래핑한 객체입니다. 다양한 도구를 정의하고 LLM과 연동하여 복잡한 작업을 수행할 수 있습니다.

```python
from langchain_community.tools import Tool

def add(x: str, y: str) -> int:
    return int(x) + int(y)

add_tool = Tool(
    name="Add",
    func=add,
    description="두 수를 더하는 도구"
)
print(add_tool.func("3", "5"))  # 8
```

### Memory

`Memory`는 대화 이력, 컨텍스트 등 상태 정보를 저장·관리하는 컴포넌트입니다. 저장된 정보를 기반으로 LLM이 더 일관성 있는 응답을 생성할 수 있도록 돕습니다.

```python
from langchain_classic.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "안녕"}, {"output": "안녕하세요!"})
memory.save_context({"input": "오늘 날씨 어때?"}, {"output": "맑아요."})
print(memory.load_memory_variables({}))
```

```bash
{'history': 'Human: 안녕\nAI: 안녕하세요!\nHuman: 오늘 날씨  어때?\nAI: 맑아요.'}
```

### Retriever

`Retriever`는 외부 문서, 데이터베이스 등에서 LLM이 필요한 정보를 검색해주는 역할을 합니다. 다양한 소스에서 관련 정보를 찾아 LLM에 제공함으로써, 더 정확하고 풍부한 응답을 생성할 수 있도록 지원합니다.

```python
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings

docs = ["LangChain은 LLM 기반 프레임워크입니다.", "AI 에이전트는 다양한 도구를 사용할 수 있습니다."]
db = FAISS.from_texts(docs, OpenAIEmbeddings())
retriever = db.as_retriever()
results = retriever.invoke("LangChain이란?")
for doc in results:
    print(doc.page_content)
```

```bash
LangChain은 LLM 기반 프레임워크입니다.
AI 에이전트는 다양한 도구를 사용할 수 있습니다.
```

---

## Reference

- [LangChain 공식 문서](https://docs.langchain.com/)

<nav class="post-toc" markdown="1">
  <h2>Table of Contents</h2>
* TOC
{:toc}
</nav>
