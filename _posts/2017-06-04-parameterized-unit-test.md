---
layout: post
title: "如何傳遞資訊進入單元測試"
modified: 2017-06-11
categories: [Python]
description:
tags: [Python, unit test]
image:
  feature:
  credit:
  creditlink:
comments:
share:
date: 2017-06-04T23:06:51+08:00
---

這個問題是當我要進行單元測試時，某個物件必須由套裝軟體產生。
因此在進行`unit test`時，就需要把這個物件當作參數傳入。

那就來看看要怎麼把資訊傳進單元測試中吧。目前找到的方法是來自於這篇  [Blog](http://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases/)。

在那篇文章中已經給出了可以使用的範例程式碼，那在更進一步理解如何使用。它可以分下列兩種方式：

1. 整個 `TestCase` 都可以取用這個參數
2. 針對不同測試單元給予不同參數

***
要開始進行的話當然要先建立一個 `Test case`, 而且必須繼承自 `ParametrizedTestCase`.
而 `ParametrizedTestCase`的程式碼，請進入 [原作者的Blog](http://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases/) 看看吧
<!--more-->
{% highlight python %}
class TestNeedPara(ParametrizedTestCase):
  def test_A(self):
    r = self.param
    self.assertEqual(10, r)
  def test_B(self):
    r = self.param*2
    self.assertEqual(20, r)
  def test_C(self):
    self.assertEqual(self.param, 3)
{% endhighlight %}

如果需求是整個 Test case 都可以取用這個變數，那就在 `addTest` 時使用 `ParametrizedTestCase.parametrize`
使每個測試單元都可以取用 `self.param`
{% highlight python %}
suite = unittest.TestSuite()
testcase1 = ParametrizedTestCase.parametrize(TestNeedPara, param=10)
suite.addTest(testcase1)
unittest.TextTestRunner(verbosity=2).run(suite)
{% endhighlight %}

執行結果：

{% highlight python %}
test_A (__main__.TestOne) ... ok
test_B (__main__.TestOne) ... ok
test_C (__main__.TestOne) ... FAIL

============================================================
FAIL: test_C (__main__.TestOne)
------------------------------------------------------------
Traceback (most recent call last):
  File "/***/***/unit_test/test.py", line 31, in test_C
    self.assertEqual(self.param, 3)
AssertionError: 10 != 3

------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)

{% endhighlight %}

另外也可以針對不同的測試區塊給予不同的參數。
例如在某個測試下`test_A` 需要 10 作為參數, `Test_B` 不需要執行， `Test_C`需要的則是 3。
那就使用比較特殊的方法產生測試單元，`TestOne(測試方法名, 參數值)`。
不過只適用於繼承 `ParametrizedTestCase`的`TestCase`就是了。

{% highlight python %}
suite = unittest.TestSuite()
suite.addTest(TestOne('test_A', 10))
suite.addTest(TestOne('test_C', 3))
unittest.TextTestRunner(verbosity=2).run(suite)
{% endhighlight %}

執行結果：

{% highlight python %}
test_A (__main__.TestOne) ... ok
test_C (__main__.TestOne) ... ok

------------------------------------------------------------
Ran 2 tests in 0.001s

OK
{% endhighlight %}
