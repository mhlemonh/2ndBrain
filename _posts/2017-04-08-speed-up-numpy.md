---
layout: post
title: "如何最佳化 Numpy 執行效率"
modified:
categories: [Python]
description:
tags: [Numpy, Python]
image:
  feature:
  credit:
  creditlink:
---

最近嘗試著要把一支用了很多 Numpy Module 的 Python 程式，盡可能地減少他的執行時間。
於是針對 Numpy 有哪些指令運作得比較慢，以及有沒有代用的寫法，就來做個整理吧！

儘管 Numpy 本身已經是一個為了數值運算而生的 Module，不過有注意幾點就可以減少運作時間。
我目前使用的版本是 1.11.0，有些運作模式會隨著版本更新進化，這點也要小心喔。

### 減少新矩陣的產生
當陣列(Array)的大小達到數十萬的時候，在計算過程中重新產生陣列會是一個很大的花費。
所以可以換成在陣列中計算的方式。

{% highlight python %}
a = np.arange(1000000)
# 比較慢, cost 1.9903 sec for 1,000 times
a = a+1

# 快一些, cost 0.9906 sec for 1,000 times
a[:] = a+1
{% endhighlight %}

### 使用 Array View
Array View 指的是使用`foo[<start index>:<end index>:<spacing>]`方法來取用數值。
不過加上一些運算後差距就沒那麼顯著了。
{% highlight python %}
a=np.arange(1000000)
i=np.arange(0,1000000,100)

# 比較慢, cost 0.4309 sec for 10,000 times
b1 = a[i]
# 快 99%, cost 0.0035 sec for 10,000 times
b2 = a[::100]

# 加上計算
# 比較慢, cost 0.0762 sec for 1,000 times
b1 = a[i] * 50
# 快 42%, cost 0.0435 sec for 1,000 times
b2 = a[::100] * 50
{% endhighlight %}
<!--
### 避免使用 Fancy indexing？
雖然曾經有搜尋過使用`Fancy indexing`會比使用`np.take`慢。不過實際使用後，應該是因為版本更新，
現在已經沒有速度差距了。

{% highlight python %}
number = np.arange(100)
minus =  np.extract(number<0, number)
{% endhighlight %}
-->
