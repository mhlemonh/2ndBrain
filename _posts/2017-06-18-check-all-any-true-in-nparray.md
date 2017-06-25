---
layout: post
title: "如何在 numpy array 中高效率判斷 (all true/any true)"
modified: 2017-06-18
categories: [Python, 效率]
description:
tags: [Python, numpy]
image:
  feature:
  credit:
  creditlink:
comments:
share:
date: 2017-06-18T21:06:51+08:00
---

在 Numpy 中如果遇上了要判斷一個 `bool array` 是否全部(all)或是任一(any)為 `True` 的時候。
在我腦中閃過得是內建的 `any()` 和 `all()` 兩個函數。不過在實際使用後發現耗費的時間意外的久。
就開始想是不是有其他的辦法加速呢？ 內建的兩個函數應當都已經有實做了提早跳出的邏輯。
推測時間應該是花在轉換和提取(不確定)？

不過既然遇上了，就嘗試幾種不同的作法，看有沒有辦法加速判斷囉。

### 計算 True 的個數
因為 `numpy` 的 `bool array` 可以用來 `indexing`，那數數看到底取出幾個 item 也就可以用來判斷有幾個 True 了！
而且結果可以直接丟進判斷式，一舉兩得。

{% highlight python %}
arr_to_check = np.random.randint(0,2, size=100000, dtype=bool)
_ = np.empty(len(array_to_check))
num_of_true = len(_[array_to_check])
# if any(arr_to_check): 可以變成
if num_of_true:
  pass
# if all(arr_to_check): 可以變成
if len(arr_to_check) == num_of_true:
  pass
{% endhighlight %}

***
### 使用 numpy 內建函數
後來拜了 Google大神後，發現原來還有`numpy.count_nonzero`可以作到一樣的事情。
而且還不用佔據額外的 `memory`。
{% highlight python %}
num_of_true = np.count_nonzero(arr_to_check)
{% endhighlight %}

***
### 效率比較

在使用 `any/all` 時可以分成兩種情況來比較：
1. 大多為 True 少數幾個為 False, 此時 all 較慢。
2. 大多為 False 少數幾個為 True, 此時 any 較慢。

下面列出兩種狀況下，比較下列三種方法：
1. 內建 `all/any` 函數
2. `indexing` 得到的長度
3. `Numpy` 內建 `count_nonzero` 函數

結果果然是使用 `numpy.count_nonzero` 各種狀況下都最快了。
使用 `indexing` 在 `almost true` 狀況下花費的時間特別多，
我想是取值時取的多花費的時間也相對多造成的。

#### 耗費時間 (sec/1000 run)

|                   | build in | indexing | count_nonzero |
|:-----------------:|:--------:|:--------:|:-------------:|
|  any(almost true) |   20.65  |  4.7434  |     0.6540    |
|  all(almost true) |  0.0022  |  4.7395  |     0.6428    |
| any(almost false) |   24.16  |  0.1847  |     0.0667    |
| all(almost false) |  0.0021  |  0.1888  |     0.0664    |


### 比較時使用的程式碼
{% highlight python %}
import numpy as np
from timeit import timeit

def build_in_any(a):
    return any(a)
def build_in_all(a):
    return all(a)
def index_any(a):
    _=np.empty(len(a))
    return bool(len(_[a]))
def index_all(a):
    _=np.empty(len(a))
    return len(a) == len(_[a])
def count_any(a):
    _=np.count_nonzero(a)
    return bool(_)
def count_all(a):
    _=np.count_nonzero(a)
    return len(a) == _
if __name__ == '__main__':

    runtimes = 1000

    setup = "from __main__ import build_in_any;\
    from __main__ import build_in_all;\
    from __main__ import index_any;\
    from __main__ import index_all;\
    from __main__ import count_any;\
    from __main__ import count_all;\
    import numpy as np;\
    true_num = np.random.randint(0,5);\
    true_location=np.random.randint(0,100000, size=true_num);\
    arr_to_check = np.full(100000, False, dtype=bool);\
    arr_to_check[true_location]=True"

    setup1 = "from __main__ import build_in_any;\
    from __main__ import build_in_all;\
    from __main__ import index_any;\
    from __main__ import index_all;\
    from __main__ import count_any;\
    from __main__ import count_all;\
    import numpy as np;\
    true_num = np.random.randint(0,5);\
    true_location=np.random.randint(0,100000, size=true_num);\
    arr_to_check = np.full(100000, True, dtype=bool);\
    arr_to_check[true_location]=False"


    print '--- build in ---'
    print timeit("build_in_any(arr_to_check)", setup=setup, number = runtimes)
    print timeit("build_in_all(arr_to_check)", setup=setup, number = runtimes)
    print '--- indexing ---'
    print timeit("index_any(arr_to_check)", setup=setup, number = runtimes)
    print timeit("index_all(arr_to_check)", setup=setup, number = runtimes)
    print '--- Numpy ---'
    print timeit("count_any(arr_to_check)", setup=setup, number = runtimes)
    print timeit("count_all(arr_to_check)", setup=setup, number = runtimes)

    print '***'
    print '--- build in ---'
    print timeit("build_in_any(arr_to_check)", setup=setup1, number = runtimes)
    print timeit("build_in_all(arr_to_check)", setup=setup1, number = runtimes)
    print '--- indexing ---'
    print timeit("index_any(arr_to_check)", setup=setup1, number = runtimes)
    print timeit("index_all(arr_to_check)", setup=setup1, number = runtimes)
    print '--- Numpy ---'
    print timeit("count_any(arr_to_check)", setup=setup1, number = runtimes)
    print timeit("count_all(arr_to_check)", setup=setup1, number = runtimes)
{% endhighlight %}
