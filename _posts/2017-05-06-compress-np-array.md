---
layout: post
title: "如何壓縮 Numpy 資料"
modified:
categories: [Python]
description:
tags: [Numpy, Python, compress, memory]
image:
  feature:
  credit:
  creditlink:
---

這次遇上的問題是在計算過程儲存了太多的 Numpy 陣列，結果居然吃到了 swap 讓系統接近當掉。
趕快搜尋有沒有什麼辦法可以減少記憶體佔用。

### 可能的作法
* 把資料先用 pickle dump 儲存到硬碟，等需要實在拿回來用。
* 相對的缺點是會有 IO 的速度耗損

***

* 壓縮 Numpy array 記在記憶體中，等需要時在解壓縮。
* 缺點是在壓縮和解壓縮時會有計算的耗損。

***

這次針對壓縮解壓縮來嘗試，搜尋到的原始教學是從 Stack Overflow[^1] 找到的。

[^1]: <http://stackoverflow.com/questions/39035983/compress-zip-numpy-arrays-in-memory>

### 壓縮方法

Numpy 本身提供一個方法 `numpy.savez_compressed`[^2] 可以把 numpy.array 以壓縮的格式
儲存在 `file` 或 `file like object` 中。如果沒有指定名稱就依序命名為 'arr_0', 'arr_1', 'arr_2'...

在原本的 Stack Overflow 中使用的是 `io.BytesIO` 來儲存。
不過後來嘗試使用 `cStringIO.StringIO()` 發現它佔用的記憶體用量更少，或許自製 File like object 會更少吧？

另外要注意的是如果資料本身是相異的話，壓縮的效果也會比較差

[^2]: <https://docs.scipy.org/doc/numpy/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed>

### 解壓縮方法

使用 `numpy.load` 來讀取，另外要注意的是 `IO` 類需要回到第一個位置開始讀取。
所以要先使用 `.seek(0)`，回到起頭處開始讀取。

{% highlight python %}
cmp_a = io.BytesIO()
cmp_b = cStringIO.StringIO()

print (sys.getsizeof(cmp_a), sys.getsizeof(cmp_b))
# obj mem size : (96, 56)

def compress(nparray, cmp_b):
    np.savez_compressed(cmp_b, nparray)


def decompress(cmp_b):
    cmp_b.seek(0)
    return np.load(cmp_b)['arr_0']

mem_cost_arr = np.array([10] * 200+[20] * 200+[18] * 200)
sys.getsizeof(mem_cost_arr)
# mem size : 4896

compress(mem_cost_arr, cmp_b)
cmp_b.seek(0)
sys.getsizeof(cmp_b.read())
# mem size : 266

decmp_arr = decompress(cmp_b)

all(mem_cost_arr == decmp_arr)
# True

{% endhighlight %}

### 測試資料重複性較低的資料

{% highlight python %}

np.random.seed(9453)
rnd_arr = np.random.randint(-10000, 10000, size=(600))

sys.getsizeof(rnd_arr)
# mem size : 4896

compress(rnd_arr, cmp_b)
cmp_b.seek(0)
sys.getsizeof(cmp_b.read())
# mem size : 1951

decmp_arr = decompress(cmp_b)

all(mem_cost_arr == decmp_arr)
# True

{% endhighlight %}
