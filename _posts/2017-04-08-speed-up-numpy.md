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

儘管 Numpy 本身已經是一個為了數值運算而生的 Module，不過有幾點特別注意就可以減少運作時間。
我目前使用的版本是 1.11.0，有些運作模式會隨著版本更新進化，這點也要小心喔。

1. 減少矩陣的複製
