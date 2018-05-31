---
layout: post
title: 在 Windows Subsystem for Linux(WSL) 中使用中文輸入法
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
date: 2018-05-29T22:03:30
---

在最近 Windows 10 推送更新後，原本在 Beta 測試的 "Bash on Ubuntu on Windows" 正式改成 WSL 並且可以在 Windows store 裡面下載安裝。所以就準備把環境從 vmware 裡的 Ubuntu 轉到 Windows 底下。結果在輸入中文遇上了麻煩，在這邊紀錄一下過程，讓自己在下次轉移時有個依靠阿。

### 狀況
1. 開啟 Dropbox 的資料夾結果全部的中文都變成了方塊字。
2. 使用 [cmder](http://cmder.net/) 可以正常從 windows 輸入中文，可是開啟其他 GUI 程式卻無法輸入中文。
3. 在其他的 GUI 都可以輸入中文的情況下，卻唯獨 sublime text 3 不能輸入。

#### 狀況1 

在執行下面的指令後就可以正常顯示了
{% highlight bash %}
sudo apt-get install fonts-noto-cjk
{% endhighlight %}

#### 狀況2 

首先安裝 fcitx 及 fcitx-chewing 
{% highlight bash %}
sudo apt-get install fcitx fcitx-chewing
{% endhighlight %}

在執行 fcitx-configtools 時除了保留 en-US 外再加入 chewing，。
接下來在 Global Config 中的 Trigger Input Method 選擇自己喜歡的快捷鍵，就完成了。

#### 狀況3 

查了一下發現有神人針對這個狀況釋出修復方法，[GitHub repo](https://github.com/lyfeyaj/sublime-text-imfix)。

照著他的作法執行，在重開 terminal 及 fcitx 就完成了。
