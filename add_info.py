#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import pandas as pd
import subprocess
from subprocess import PIPE

def by_dig(domains):
    # dig domain
    domain_digres = dict()
    for domain in domains:
        res = subprocess.run('dig ' + domain + ' +noques +nocomments +nostats +nocmd', shell=True, stdout=PIPE, stderr=PIPE)
        res_list = res.stdout.decode('utf-8').split("\n")
        domain_digres[domain] = list()
        for line in res_list[3:-1]:
            domain_digres[domain].append(line)

    ip_num = 0
    dig_info = list()

    for k, v in domain_digres.items():
        ip_num = len(v)
        cache_time = 0
        
        # ipの結果
        for res in v:
            res_list =  res.split()
            if len(res_list) == 0:
                continue
                
            # キャッシュの時間を足していく
            if is_num(res_list[1]):
                cache_time += int(float(res_list[1]))
            
            # CNAMEだった場合、ipの数を減らす
            if len(res_list) > 3 and res_list[3] == 'CNAME':
                ip_num = ip_num - 1
        
        if len(v) == 1:
            dig_info.append([k, ip_num, cache_time])
        elif len(v) == 0:
            dig_info.append([k, ip_num, 0])        
        else:
            dig_info.append([k, ip_num, cache_time/len(v)])

    df = pd.Dataframe(
        dig_info, 
        index=[
            'domain',
            'ip_num',
            'cache_time']
    ) 

    return df
