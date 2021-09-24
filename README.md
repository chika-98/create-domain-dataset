# create-domain-dataset

## discription
- you can get the domain dataset from urls if you use this scripts.
- this method has the part that uses dig command.
- features of the data　created：

| feature name | discription |
|---|---|
|domain| the name of domain(string） |
|url_length| the mean of URL length|
|url_number_character| URL内にある数字[0-9]の数の平均|
|num_of_path| URLのパスの深さの平均|
|xls_url|URL extension is .xls（y：１、n：０）|
|doc_url|URL extension is .doc（y：１、n：０）|
|zip_url|URL extension is .zip（y：１、n：０）|
|domain_length|the length of domain|
|domain_number_character|Ratio of numbers to domain length(%)|
|ip_address|Domain is in the form of an IP address(yes:1, no:0)|
|localhost|Domain is in the form of localhost(yes:1, no:0)|
|ip_num| number of ips|
|cache_time| the mean of cache_time |

---

## how to use

you should make directory 'dataset' first.
```
mkdir create-domain-dataset/dataset
```

Run the prepared URLs in a script

```
cat {URLfile} | python3 create-domain-dataset/main.py
```

or

```
echo {URL} | python3 create-domain-dataset/main.py
```

the file {%Y%m%d}.tsv will be created under 'dataset'
