#!/usr/bin/env/python
# -*- coding: utf-8 -*-

# domain操作用ツール

# IPアドレスか判定（ポート付きもOK）
# 引数：ドメイン
def is_ip(domain):
    m = re.match('(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])', domain)
    if m:
        return(True)
    else:
        return(False)

# localhostか判定
def is_localhost(domain):
    m = re.match('(^127\.)|(^169\.254\.)|(^10\.[0-9])|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)', domain)
    if m:
        return(True)
    else:
        n = re.match('(^localhost$)|(^localhost:)', domain)
        if n:
            return(True)
        return(False)    

def parcentage_number_character(domain):
    return int(len(re.findall('\d', domain))*100 /  len(domain.replace('.', '')))