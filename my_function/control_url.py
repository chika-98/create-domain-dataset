#!/usr/bin/env/python
# -*- coding: utf-8 -*-

# URL操作用ツール

import re
from urllib.parse import urlparse

# パラメータ除去
# 引数：URL
def remove_parameter(URL):
    return(re.sub("\?.+", "", URL))

# domain取り出し
# 引数：URL
def domain(URL):
    return(urlparse(URL).netloc)

# pathの深さを返す
def count_path(URL):
    # path部分のみ取り出し
    path = urlparse(URL).path

    new_path1 = re.sub('^/', '', path)
    new_path2 = re.sub('/$', '', new_path1)
    if len(new_path2) == 0:
        return 0
    return len(new_path2.split('/'))

# .docで終わるURLか
def is_doc(URL):
    pattern = re.compile(r'\.doc$')
    return bool(pattern.search(URL))

# .xlsで終わるURLか
def is_xls(URL):
    pattern = re.compile(r'\.xls$')
    return bool(pattern.search(URL))

# .zipで終わるURLか
def is_zip(URL):
    pattern = re.compile(r'\.zip$')
    return bool(pattern.search(URL))

def count_number_character(URL):
    return int(len(re.findall('\d', URL)))


