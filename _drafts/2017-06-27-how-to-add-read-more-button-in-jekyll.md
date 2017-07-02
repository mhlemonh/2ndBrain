---
layout: post
title: 如何在 Jekyll 中加入 Read more 按鈕
modified:
categories: Blog
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

### 旅程摘要

1. 確認 `excerpt_separator` 的運作方法
{% raw %}
2. 找不到 `{{ content }}` 的取代檔案，只好重寫 `home.html` 來修改產生 `Read more` 按鈕的區塊
{% endraw %}
3. 影響到其他使用 `home layout` 頁面拉，大爆炸。快分開頁面的關聯。
{% raw %}
4. 發現 `home.html` 是 layout 要修改的應該是！
{% endraw %}
5. 減少修改數量，去除額外的 `layout`，完成！

<!--more-->

接下來我一步步走歪了，不過我有多學到一些就是了。看解法直接到[這邊](#anchor).

### 確認 `excerpt_separator` 運作方法

在 Jekyll 中是使用 [Liquid template language](https://shopify.github.io/liquid/)
來動態讀取內容再產生頁面。而設定 `excerpt_separator` {% raw %}會使的 `{{ post.content }}`
與 `{{ post.excerpt }}` {% endraw %}產生差異，分別顯示全文和顯示`excerpt_separator`前的摘要文字。

### 重寫 `home.html` 來修改產生 `Read more` 按鈕的區塊

但是我那都找不到 {% raw %} `{{ post.excerpt }}` {% endraw %}出現的地方。在 `home.html`
裡面就只有{% raw %} `{{ content }} ` {% endraw %}存在，只好把 `home.html` 重寫。

> 這邊是錯誤的，`home.html` 是 layout，用來讓 `index.html` 等參考的頁面。所以應該修改的是 `index.html`。

### 影響到其他使用 `home layout` 頁面

### {% raw %} {{ content }} 的取用邏輯{% endraw %}

<a id="anchor"></a>

### 最後修整！
