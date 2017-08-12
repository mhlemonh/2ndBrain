#!/usr/bin/python

import sys
import time

def creat_newpost(post_name):
	# current_time = time.time()
	post_url = '-'.join(post_name.split())
	post_date = time.strftime('%Y-%m-%d')
	post_time = time.strftime('%Y-%m-%dT%H:%M:%S')
	post_path = './{}-{}.md'.format(post_date, post_url)
	init_content = \
"""---
layout: post
title: {} 
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
date: {}
---
""".format(post_name, post_time)
	with open(post_path, 'w') as newpost:
		newpost.write(init_content)

if __name__ == '__main__':
	post_name = sys.argv[1]
	creat_newpost(post_name)