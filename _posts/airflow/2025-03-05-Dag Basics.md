---
title: DAG Basics
category: Airflow
tag: [DAG, Airflow]
---

> DAG(Directed Acyclic Graph)는 Airflow에서 워크플로우를 정의하는 기본 단위로, Python 코드로 작성되며 여러 개의 Task로 구성됩니다. 각 Task의 실행 순서와 종속성을 정의할 수 있으며, 주어진 일정에 따라 자동으로 실행되어 데이터 파이프라인을 효과적으로 관리할 수 있습니다.

---

## Basic Structure

Airflow에서 `DAG`는 아래와 같은 기본 구조를 가집니다.

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# 기본 설정
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 2, 2),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# DAG 정의
dag = DAG(
    "my_first_dag",
    default_args=default_args,
    description="My first Airflow DAG",
    schedule_interval="@daily",
    catchup=False,
)

# 실행할 함수 정의
def print_hello():
    print("Hello, Airflow!")

# Task 정의
task_1 = PythonOperator(
    task_id="print_hello",
    python_callable=print_hello,
    dag=dag,
)

task_2 = BashOperator(
    task_id="echo_hello",
    bash_command="echo 'Hello, Airflow!'",
    dag=dag,
)

task_1 >> task_2
```

---

## Operators

Airflow에서는 다양한 오퍼레이터를 제공하여 `DAG` 내에서 여러 작업을 수행할 수 있습니다.

### PythonOperator

`PythonOperator`는 `Python` 함수를 실행하는 데 사용됩니다.

```python
def my_python_function():
    print("Hello from PythonOperator")

python_task = PythonOperator(
    task_id="python_task",
    python_callable=my_python_function,
    dag=dag,
)
```

### BashOperator

`BashOperator`는 `Bash` 명령어를 실행할 때 사용됩니다.

```python
from airflow.operators.bash import BashOperator

bash_task = BashOperator(
    task_id="bash_task",
    bash_command="echo 'Hello from BashOperator'",
    dag=dag,
)
```

### DummyOperator

`DummyOperator`는 실행 없이 단순히 `Task` 간의 의존성을 설정할 때 사용됩니다.

```python
from airflow.operators.dummy import DummyOperator

dummy_task = DummyOperator(
    task_id="dummy_task",
    dag=dag,
)
```

---

## Task Dependencies

Airflow에서는 `>>` 연산자를 사용하여 `Task` 간의 실행 순서를 정의할 수 있습니다.

```python
python_task >> bash_task >> dummy_task
```

### Parallel Task

여러 `Task`를 동시에 실행할 수도 있습니다. 이를 통해 의존성이 없는 작업들을 병렬로 처리하여 파이프라인의 효율성을 높일 수 있습니다.

```python
python_task >> [bash_task, dummy_task] # bash_task, dummy_task 동시 실행
```

---

## References

- [Airflow 공식 문서](https://airflow.apache.org/docs/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
