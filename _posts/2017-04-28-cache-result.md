---
layout: post
title: "暫存執行結果來加快執行速度"
modified:
categories: [Python, 效率]
description:
tags: [cache, Python]
image:
  feature:
  credit:
  creditlink:
---

在拆分 function 時，遇上 function 執行的時間花費太高，又重複使用相同輸入值很多次。
就可以考慮暫存運算結果，降低計算花費。

### 特徵化輸入值
相同的輸入值必須有相同的特徵值，反之不同的輸入值相對應的特徵值也必須不同。
想的到的方法有：
1. 把輸入值組成 `tuple`，成為不變的特徵
2. 計算輸入值的特徵 id

### 儲存計算後得結果
把計算的結果和特徵值連結，當有新的輸入值出現先和結果池比對。

***

下面是查到的幾種作法：
#### 1. 計算過程中儲存結果
{% highlight python %}
input = np.random.randint(1, 5, size=(3,1000))

cache = {}
for i in range(100000):
  a, b, c = input[0,i], input[1,i], input[2,i]
  input_id = tuple([a, b, c])
  if input_id in cache:
    return cache[input_id]
  else:
    result = long_runtime_func(a, b, c)
    cache[input_id] = result
    return result
{% endhighlight %}
