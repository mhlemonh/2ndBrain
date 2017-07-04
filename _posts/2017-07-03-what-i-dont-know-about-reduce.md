---
layout: post
title: 我之前不知道的 Reduce 特性
modified:
categories: [Python]
description:
tags: [Python]
image:
  feature:
  credit:
  creditlink:
comments:
share:
date: 2017-07-03T22:13:16+08:00
---

`reduce`, `map` 和 `filter` 是三個經常一起出現，針對可迭代物件特殊處理的函式。

最近在使用 `reduce` 時遇上了一個想不通的 bug。結果是因為不夠了解 reduce 本身的運作方法。

在 python 2.7 的[說明文件](https://docs.python.org/2/library/functions.html#reduce)中，沒注意到的是這個部份：

>If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned. Roughly equivalent to:

{% highlight python%}
def reduce(function, iterable, initializer=None):
   it = iter(iterable)
   if initializer is None:
       try:
           initializer = next(it)
       except StopIteration:
           raise TypeError('reduce() of empty sequence with no initial value')
   accum_value = initializer
   for x in it:
       accum_value = function(accum_value, x)
   return accum_value
{% endhighlight %}

### 遇上的 Bug

在針對 2D numpy bool array 進行行(row)與行之間的 `logical_and` 處理。想要針對多種
行數組合取得結果。在重新對原始 2D array 進行 in-place 處理。結果在某次只傳入一行後，針對
原始數據修改，使的結果也改變了。

總的來說，有幾個結論：
1. 要看清楚 document
2. 在處理 numpy array 時，參照的記憶體位置是不是新的，會不會修改到其他部份的值。
