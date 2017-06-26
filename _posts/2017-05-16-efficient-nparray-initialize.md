---
layout: post
title: "高效率的初始化 Numpy array"
modified:
categories: [Python, 效率]
description:
tags: [numpy, Python]
image:
  feature:
  credit:
  creditlink:
---

初始化一個 `Numpy array` 的花費其實只是一個很小的比例。不過把各種可能的加速方法組合在一起，也不失是一個最佳化的辦法。
然而在 `python` 中應該也要維持 `pythonic`，這兩點還須要自己權衡一下。

### 初始化方法
在 Numpy 中提供了幾種基本方法。`np.ones`, `np.zeros`, `np.empty`, `np.fill` 和 `np.full`。
有下面幾種作法：
1. 建立一個全部都是1的陣列在乘上特定值。
2. 組合 `np.empty` 和 `np.fill`，先取得記憶體位置再填滿初值。
3. 直接使用內建 `np.full` 完成目標。
<!--more-->
***

### 速度比較
{% highlight python %}
def method1(array_len, initial_val):
    ini_arr = np.ones(array_len) * initial_val
    return ini_arr

def method2(array_len, initial_val):
    ini_arr = np.empty(array_len)
    ini_arr.fill(initial_val)
    return ini_arr
def method3(array_len, initial_val):
    ini_arr = np.full(array_len, initial_val)
    return ini_arr

if __name__ == '__main__':
    setup_stmt = \
      'from __main__ import method1;
       from __main__ import method2;
       from __main__ import method3;
       import numpy as np'
    timeit('method1(10000, 7.3)', setup = setup_stmt, number=10000)
    # Time cost: 0.141 s
    timeit('method2(10000, 7.3)', setup = setup_stmt, number=10000)
    # Time cost: 0.086 s
    timeit('method3(10000, 7.3)', setup = setup_stmt, number=10000)
    # Time cost: 0.103 s
{% endhighlight %}

### 總結

總的來說，雖然方法 2能用最小的時間達成目標，不過為了顧及 `pythonic`，還是
用 `np.full(size, val)` 比較好。
