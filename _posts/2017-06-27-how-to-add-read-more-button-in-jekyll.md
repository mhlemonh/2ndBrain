---
layout: post
title: 如何在 Jekyll 中加入 Read more 按鈕
modified:
categories: [Blog]
description:
tags: [Jekyll]
image:
  feature:
  credit:
  creditlink:
comments:
share:
date: 2017-06-27T22:13:16+08:00
---

這個 Blog 使用的是 [Neo-HPSTR](https://github.com/aron-bordin/neo-hpstr-jekyll-theme)
的主題。不過當我寫了比較長的文章後，卻遇上了要捲動實在太久的麻煩。

雖然 `Jekyll` 本身支援在 `_config.yml` 中設定摘要標籤(`excerpt_separator`)。
使的首頁只顯示文章摘要。但在使用後發現 `Read more` 按鈕並沒有出現！就開始了找問題的旅程了。

## 旅程摘要

1. 確認 `excerpt_separator` 的運作方法
{% raw %}
2. 找不到 `{{ content }}` 的取代檔案，只好重寫 `home.html` 來修改產生 `Read more` 按鈕的區塊
{% endraw %}
3. 影響到其他使用 `home layout` 頁面拉，大爆炸。快分開頁面的關聯。
{% raw %}
4. 發現 `home.html` 是 layout 要修改的應該是 `index.html`！
{% endraw %}
5. Bug 居然是這裡！不過繞路的過程多了解了不少東西呢！

<!--more-->

接下來我一步步走歪了，不過我有多學到一些就是了。看解法直接到[這邊](#anchor).

## 確認 `excerpt_separator` 運作方法

在 Jekyll 中是使用 [Liquid template language](https://shopify.github.io/liquid/)
來動態讀取內容再產生頁面。而當文章中含有 `excerpt_separator` 會使的{% raw %} `{{ post.content }}`
與 `{{ post.excerpt }}` {% endraw %}產生差異，分別顯示全文和顯示`excerpt_separator`前的摘要文字。

## 重寫 `home.html` 來修改產生 `Read more` 按鈕的區塊

但是我那都找不到 {% raw %} `{{ post.excerpt }}` {% endraw %}出現的地方。在 `home.html`
裡面就只有{% raw %} `{{ content }} ` {% endraw %}存在，只好把 `home.html` 重寫。

> 這邊是錯誤的，`home.html` 是 layout，用來讓 `index.html` 等參考的頁面。所以應該修改的是 `index.html`。

重寫的過程比較值得提的部份是，如何判斷{% raw %} `{{ post.excerpt }}` {% endraw %}到底是否為摘要後的結果。
這有兩種方法：
1. 判斷{% raw %} `{{ post.content }}` {% endraw %}有沒有包含(使用 contains operator)
`excerpt_separator`。
2. 用 `number_of_words` 判斷{% raw %} `{{ post.content }}`和`{{ post.excerpt }}`
{% endraw %}內部的字數是否相同。

<a id="anchor"></a>

## 問題點居然是？

換了方法2後就Read more按鈕就正常出現了，難道是因為中文的關係讓方法1發生錯誤了嘛？
經過多個測試後發現，居然是因為我不經意改動了`excerpt_separator`的設定。

> 從 \<!\-\- more \-\-> 變成 \<!\-\-more\-\-> ，中間少了兩個空格。

結果是白忙了一場阿，不過過程中多了解了 Liquid template language 的基本運作
和 Jekyll 的大略架構。也算是不錯的體驗。

### 增加 Read more 按鈕的方法

要做出含有摘要及 `Read more` 按鈕的主頁(index)，需要先知道這幾項變數：
{% raw %}
* {{ post.content }} 顯示文章的全文
* {{ post.excerpt }} 顯示文章在`excerpt_separator`前的部份
* {{ post.title }} 文章的標題(title)
* {{ post.url }} 文章的網址連結
* {{ site.url }} blog的主網域，在 `_config` 中設定
{% endraw %}
更詳細內容在[怎麼發表/寫文章](https://jekyllrb.com/docs/posts/)，
和[Template的用法](https://jekyllrb.com/docs/templates/)。

接下來就是簡化的程式碼，完整的內容可以看這個主題的[index.html](https://github.com/aron-bordin/neo-hpstr-jekyll-theme/blob/master/index.html)
{% highlight html %}
{% raw %}
<ul>
  {% for post in site.posts %}
    <div>
      <h1><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></h1>
    </div>
    <div>
    {{ post.excerpt}}
    {% if post.content contains "<!--more-->" %}
      <div align="right">
        <a href="{{ site.url }}{{ post.url }}" class="btn btn-primary">Read more ...</a>
      </div>
    {% endif %}
    </div>
  {% endfor %}
</ul>
{% endraw %}
{% endhighlight %}
