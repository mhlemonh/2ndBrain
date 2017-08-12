---
layout: post
title: 如何加快緩慢的 Numpy for 循環
modified:
categories:
description:
tags:
image:
  feature:
  credit:
  creditlink:
comments:
share:
date: 2017-08-12T12:30:14CST
---

在使用 `Numpy` 的過程中，儘管知道要最大化程式執行效率，需要將數值處理方法 `Vectorizing`。
不過還是會遇上不管怎麼想也想不到`for loop`以外的方法。只好忍痛用下去，最後卻發現效率降低的好快。

進去檢查後發現，原來是 `for loop` 和 `Numpy` 搞的鬼。儲存在 `Numpy array` 中的數據資料，
要讓 `for loop` 取用的時候會需要做型態轉換，此時執行效率耗損就發生了。

遇到這種狀況，我的解決辦法就是：
> 先把 `Numpy array` 使用 `tolist()` 一口氣轉成 `list` 型態，這樣就可以方便 `for loop`
的取用。在我的實際例子中，可以最多降低 50％ 的執行時間呢。
