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

在平常使用 `format()` 的時候都只有用到 `"{}.{}".format(index, msg)` 這種程度的字串取代。但是最近想寫一個在 Terminal 下顯示與 `git log --graph` 類似的小 module，於是搜尋整理一下 `format` 的用法。

---

## Format syntax：

`Format syntax` 就是放置在固定字串中以花括號 `{}` 包圍，用來表示取得及處理字串的方法。

詳細來說，花括號中有三個可填選項，依序分別是`[field_name]` `[conversion]` `[format_spec]`

最簡單的例子是留空，都使用 `default` 效果，把傳入的 argument 不經處理，依序填入。
{% highlight python %}
replace_string = "pen"
print "This is a {}.".format(replace_string)
# This is a pen.
{% endhighlight %}
<!--more-->
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

-- 待續 --

### Reference:

* [Format String Syntax](https://docs.python.org/2/library/string.html#format-string-syntax)