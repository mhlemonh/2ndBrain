---
layout: post
title: Python 2.7 Format 使用筆記
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
date: 2018-06-03T14:30:26
---

在平常使用 `format()` 的時候都只有用到 `"{}.{}".format(index, msg)` 這種程度的字串取代。但是最近想寫一個在 Terminal 下顯示與 `git log --graph` 類似的小 module，於是搜尋整理一下 `format` 的特殊用法([來源](https://mkaz.blog/code/python-string-format-cookbook/)) 和文件囉。

---

# 特殊用法

## 將 format 作為 function 使用

這其實是把字串的format函數重新命名來使用喔。

{% highlight python %}

greeting = "Hi, my name is {name}, nice to meet you.".format

print greeting(name="Jack")

# Hi, my name is Jack, nice to meet you.
{% endhighlight %}


## 由參數給出 Format syntax 

花括號中的顯示設定也可以由 format 參數指定。

{% highlight python %}
formatted_string = "{:{fill}{align}{width}}"
for align_method in ["<", "^", ">"]:
    print formatted_string.format("***",
                                  fill="-",
                                  align=align_method,
                                  width="9")
# ***------
# ---***---
# ------***
{% endhighlight %}

---

<!--more-->

# 文件整理

## Format syntax：

`Format syntax` 就是放置在固定字串中以花括號 `{}` 包圍，用來表示取得及處理字串的方法。

詳細來說，花括號中有三個可填選項，依序分別是`[field_name]` `[conversion]` `[format_spec]`

最簡單的例子是留空，都使用 `default` 效果，把傳入的 argument 不經處理，依序填入。
{% highlight python %}
replace_string = "pen"
print "This is a {}.".format(replace_string)
# This is a pen.
{% endhighlight %}

field_name
==========

field_name 必需是鍵值 `key` 或整數 `integer` 。如果輸入的是整數會以傳入的順序取值，鍵值則會去尋找 `format()` 的命名參數。此外這兩種定義方法都可以在後面加上 `.name` 或 `[index]` 去分別取用傳入物件的 `gtattr()` 或 `__getitem__()` 方法。
{% highlight python %}

print "This is a {1}, not a {0}.".format("cat","dog")
# This is a dog, not a cat.

print "This is a {stationery}.".format(stationery="pen")
# This is a pen.

item_dict = {'stationery':'pen',
             'decoration':'paint'}
print "This is a {decoration}.".format(**item_dict)
# This is a paint.

item_list = ['desk', 'chair']
print "This is a {item_list[0]}.".format(item_list=item_list)
# This is a desk.

class ball(object):
    def __init__(self, color):
        self.color = color

baseball = ball("white")
print "Baseball is {ball.color}.".format(ball=baseball)
# Baseball is white.

{% endhighlight %}

conversion
==========

要使用 conversion 這個功能的話的開頭必存在 `"!"`，目前可以選用的只有 `"s"` 或 `"r"`。 分別代表使用傳入物件的 `str()`(default) 或是 `repr()` 函數來取得帶入字串。

{% highlight python %}
class ball(object):
    """docstring for ball"""
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return "{} ball".format(self.color)
    def __repr__(self):
        return "<ball object, color = '{}'>".format(self.color)

baseball = ball("white")
print "This is a {!s}.".format(baseball)
# This is a white ball
print "Show repr: {!r}.".format(baseball)
# Show repr: <ball object, color = 'white'>
{% endhighlight %}

format_spec
===========

這個部份算是最常用到的，有點像一個簡單的程式語言。他的建立規則如下：

`[[填充字元]對齊方位][正負號][#][0][字串寬度][,][.小數點位數][顯示類別]`

|       | 選項    |意義|
|:----:|:----:|----|
|填充字元| 任意字元 |當輸入字串長度少於`字串寬度`時，用來補齊的字元。|
|=====
|對齊方位| <    |向左對齊|
|       | ^    |置中對齊|
|       | >    |向右對齊|
|       | =    |只可用於數值。如果正負號存在，則指定其落在第一個字元。|
|=====
|正負號| +    |當輸入值是數字時，不論正負值都分別在前方加上正、負號。|
|     | -    |當輸入值是數字時，只在負數前加上負號。|
|     | 空白字元|當輸入值是數字時，在正數前加上空白，在負數前加上負號。|
|=====
|＃       |加/不加|當輸入值是數字而且被轉成"hexadecimal", "octal" 或
|         |      | "binary"時在前方分別加上 [0x]，[0o]，[0b]。|
|=====
|0        |加/不加|等同於設定：填充字元為"0 "，對齊方位為"= "。|
|=====
|字串寬度  | 整數  |指定至少佔據多少字元。當字串長度比指定寬度短時，就使用
|         |      |填充字元補滿。|
|=====
|,        |加/不加|是否使用逗號作為千位數分隔。|
|=====
|.小數點位數|      |只能在浮點數使用，定義顯示小數點後幾位。|
|=====
|顯示類別  | b     |轉成二進制(Binary)。|
|(整數)   | c     |轉成 Unicode 對應的字元。|
|         | d     |預設值，十進制顯示。|
|         | o     |轉成八進制(Octal)。|
|         | x     |轉成"大寫"十六進制(Hexadecimal)。|
|         | X(大寫)|轉成"小寫"十六進制(Hexadecimal)。|
|=====
|顯示類別  | e, E  |科學記號表示，其大小寫影響以大寫或小寫顯示e。|
|(浮點數)  | f, F  |小數表示，預設顯示位數為 6。|
|         | g, G  |自動依照顯示位數選擇使用科學記號或一般表示，
|         |       |預設顯示位數為 6，大小寫影響科學記號表示。|
|         | %     |百分為顯示，等同於自動乘上 100。|
|=====
||||
{: rules="groups"}


## Reference:

* [7.1. string  Common string operations](https://docs.python.org/2/library/string.html#format-string-syntax)
* [Python String Format Cookbook](https://mkaz.blog/code/python-string-format-cookbook/)