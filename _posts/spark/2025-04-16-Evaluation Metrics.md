---
title: Evaluation Metrics
category: Spark
tag: [SparkML, Spark]
---

> SparkML은 대규모 데이터를 처리하는 머신러닝 라이브러리로, 모델 학습과 예측을 지원합니다. 모델의 성능을 평가하는 것은 중요한데, 이를 통해 예측 정확도나 클러스터링 성능을 확인하고 개선할 수 있습니다. 다양한 평가 지표를 제공하여 모델을 최적화하고, 데이터 기반 의사결정을 돕습니다.

---

## Regression

### RMSE 
**RMSE(Root Mean Squared Error, 평균 제곱근 오차)**는 예측값과 실제 값의 차이를 제곱하여 평균을 구한 후, 그 제곱근을 취한 값입니다. 이 값이 작을수록 모델의 예측 정확도가 높다는 것을 의미합니다. `RMSE`는 오차의 크기를 직관적으로 나타내는 데 유용합니다. 값이 `0`에 가까울수록 모델의 예측이 더 정확하다는 의미입니다.

```python
from pyspark.ml.evaluation import RegressionEvaluator

evaluator = RegressionEvaluator(labelCol="value", predictionCol="prediction", 
                                metricName="rmse")
rmse = evaluator.evaluate(predictions)
print(f"RMSE: {rmse}")
```

```bash
RMSE: 1.43037925984368e-12
```

### R²
**R²(R-squared, 결정 계수)**는 모델이 데이터의 분산을 얼마나 잘 설명하는지 나타내는 지표로, `1`에 가까울수록 모델이 데이터를 잘 설명하는 것입니다. 0에 가까운 값은 모델이 데이터의 변동성을 거의 설명하지 못함을 의미합니다. `R²`는 모델의 적합도를 평가하는 데 유용합니다.

```python
from pyspark.ml.evaluation import RegressionEvaluator

evaluator = RegressionEvaluator(labelCol="value", predictionCol="prediction", 
                                metricName="r2")
r2 = evaluator.evaluate(predictions)
print(f"R²: {r2}")
```

```bash
R²: 1.0
```

### MAE 
**MAE(Mean Absolute Error, 평균 절대 오차)**는 예측값과 실제 값의 차이를 절대값으로 계산하여 그 평균을 구한 값입니다. 값이 `0`에 가까울수록 모델의 예측이 더 정확하다는 의미입니다. `MAE`는 예측값의 정확성을 직관적으로 보여주며, 제곱 오차가 아닌 절대 오차를 사용하여 큰 오차에 대해 과도한 패널티를 주지 않습니다.

```python
from pyspark.ml.evaluation import RegressionEvaluator

evaluator = RegressionEvaluator(labelCol="value", predictionCol="prediction", 
                                metricName="mae")
mae = evaluator.evaluate(predictions)
print(f"MAE: {mae}")
```

```bash
MAE: 1.0708356070730839e-12
```

### MSE 
**MSE(Mean Squared Error, 평균 제곱 오차)**는 예측값과 실제 값의 차이를 제곱하여 평균을 구한 값입니다. `RMSE`와 유사하지만, 제곱근을 취하지 않기 때문에 값이 작을수록 더 좋은 모델입니다. `MSE`는 큰 오차에 대해 더 큰 패널티를 부여하여, 큰 오차를 줄이는 데 중요한 역할을 합니다.

```python
from pyspark.ml.evaluation import RegressionEvaluator

evaluator = RegressionEvaluator(labelCol="value", predictionCol="prediction", 
                                metricName="mse")
mse = evaluator.evaluate(predictions)
print(f"MSE: {mse}")
```

```bash
MSE: 2.045984826990954e-24
```

---

## Classification

### Accuracy
**Accuracy(정확도)**는 전체 데이터 중에서 정확하게 분류된 데이터의 비율을 의미합니다. 모델이 예측한 값이 실제 값과 얼마나 일치하는지를 나타내는 지표로, 값이 `1`에 가까울수록 모델이 잘 분류한 것입니다. 그러나 클래스 불균형이 심한 경우에는 정확도가 높은 것만으로는 좋은 모델이라고 평가할 수 없습니다.

```python
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="value", predictionCol="prediction", 
                                              metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Accuracy: {accuracy}")
```

```bash
Accuracy: 0.8162251655629139
```

### Precision
**Precision(정밀도)**는 모델이 예측한 Positive 클래스 중에서 실제로 Positive인 데이터의 비율을 의미합니다. 값이 `1`에 가까울수록 모델이 예측한 Positive가 실제로 맞았다는 뜻입니다. 정밀도는 모델이 얼마나 정확하게 긍정적인 예측을 했는지를 평가하는 지표입니다.

```python
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="value", predictionCol="prediction", 
                                              metricName="weightedPrecision")
precision = evaluator.evaluate(predictions)
print(f"Precision: {precision}")
```

```bash
Precision: 0.8170603530840838
```

### Recall
**Recall(재현율)**은 실제 Positive 클래스 중에서 모델이 예측한 Positive의 비율을 의미합니다. 값이 `1`에 가까울수록 모델이 실제 Positive를 잘 잡았다는 뜻입니다. 재현율은 모델이 실제 긍정적인 예시를 얼마나 잘 식별했는지를 나타냅니다.

```python
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="value", predictionCol="prediction", 
                                              metricName="weightedRecall")
recall = evaluator.evaluate(predictions)
print(f"Recall: {recall}")
```

```bash
Recall: 0.8162251655629139
```

### F1
`F1-score`는 `Precision`과 `Recall`의 균형을 맞춘 값입니다. 정밀도와 재현율이 둘 다 높을 때 F1-score도 높습니다. F1-score는 두 지표가 잘 맞는지를 평가하며, 값이 `1`에 가까울수록 모델이 잘 동작한다는 뜻입니다. 주로 정밀도와 재현율의 균형이 중요한 상황에서 유용합니다.

```python
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# F1-score 계산
evaluator = MulticlassClassificationEvaluator(labelCol="value", predictionCol="prediction", 
                                              metricName="f1")
f1_score = evaluator.evaluate(predictions)
print(f"F1-score: {f1_score}")
```

```bash
F1-score: 0.815993482890897
```

### AUC 
**AUC (Area Under the Curve, 곡선 아래 면적)**는 `ROC Curve` 아래 면적을 의미합니다. `AUC`는 모델의 분류 성능을 평가하는 지표로, 값이 `1`에 가까울수록 모델이 잘 예측했다는 의미입니다. AUC가 0.5이면 모델이 랜덤 예측을 하는 것과 같고, `1`에 가까울수록 매우 좋은 모델로 평가됩니다.

```python
from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator(labelCol="value", rawPredictionCol="prediction", 
                                          metricName="areaUnderROC")
auc = evaluator.evaluate(predictions)
print(f"AUC: {auc}")
```

[![](\assets\posts\2025-04-16-Evaluation Metrics.md\auc.png)](\assets\posts\2025-04-16-Evaluation Metrics.md\auc.png)

```bash
AUC: 0.815708660985534
```

---

## Clustering

### Silhouette
`Silhouette Score`는 클러스터링 결과가 얼마나 잘 분리되었는지 평가하는 지표입니다. 각 데이터 포인트가 자신이 속한 클러스터와 얼마나 가까운지, 그리고 다른 클러스터와 얼마나 멀리 떨어져 있는지를 기반으로 점수를 계산합니다. 값은 -1에서 1 사이로, 값이 `1`에 가까울수록 클러스터가 잘 분리되었다는 의미입니다.

```python
from pyspark.ml.evaluation import ClusteringEvaluator

evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print(f"Silhouette Score: {silhouette}")
```

```bash
Silhouette Score: 0.7475653709556944
```

---

## References
- [Spark 공식 문서](https://spark.apache.org/docs/latest/)

<nav class="post-toc" markdown="1">
  <h2>Contents</h2>
* TOC
{:toc}
</nav>
