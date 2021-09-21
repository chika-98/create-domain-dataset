#!/usr/bin/env/python
# -*- coding: utf-8 -*-

# urlからdomainのデータセットを作成するツール

import sys
import add_info
from urllib.parse import urlparse
from my_function import control_url, control_domain
import pandas as pd
import statistics

def get_base_df(urls):
    df_dict = dict()
    for url in urls:
        domain = control_url.domain(url)
        if domain not in df_dict.keys():
            df_dict[domain] = {
                'url_length': [],
                'url_number_character': [],
                'num_of_paths': [],
                'xls_url': 0,
                'doc_url': 0,
                'zip_url': 0,
                'domain_length': 0,
                'domain_number_character': 0,
                'ip_address': 0,
                'localhost': 0
            }
            df_dict[domain]['domain_length'] = len(domain)
            df_dict[domain]['domain_number_character'] = control_domain.parcentage_number_character(domain)
            if control_domain.is_ip(domain):
                df_dict[domain]['ip_address'] = 1
            if control_domain.is_localhost(domain):
                df_dict[domain]['localhost'] = 1

        df_dict[domain]['url_length'].append(len(url))
        df_dict[domain]['url_number_character'].append(control_url.count_number_character(url))
        df_dict[domain]['num_of_paths'].append(control_url.count_path(url))
        if control_url.is_xls(url):
            df_dict[domain]['xls_url'] = 1
        if control_url.is_doc(url):
            df_dict[domain]['doc_url'] = 1
        if control_url.is_zip(url):
            df_dict[domain]['zip_url'] = 1
    
    df_list = []
    for k, v in df_dict.items():
        df_list.append([
            k, 
            statistics.mean(v['url_length']), 
            statistics.mean(v['url_number_character']),
            statistics.mean(v['num_of_paths']),
            v['xls_url'],
            v['doc_url'],
            v['zip_url'],
            v['domain_length'],
            v['domain_number_character'],
            v['ip_address'],
            v['localhost']])
    
    df = pd.DataFrame(
        df_list, 
        columns=[
            'domain', 
            'url_length', 
            'url_number_character', 
            'num_of_path', 
            'xls_url', 
            'doc_url', 
            'zip_url', 
            'domain_length', 
            'domain_number_character',
            'ip_address',
            'localhost']
        )
    return df

def main(urls):
    domains = set()
    for url in urls:
        domains.add(urlparse(url).netloc)

    base_df = get_base_df(urls)
    dig_info = add_info.by_dig(domains)
    return pd.merge(base_df, dig_info)


if __name__ == "__main__":
    urls =  set([line.strip() for line in sys.stdin])
    df = main(urls)
