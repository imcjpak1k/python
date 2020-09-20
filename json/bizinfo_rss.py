import json
import chardet

rss_dict = None
encoding = 'utf-8'

# encoding check
with open('c:/Users/imcjp/workspace/vscode/python/json/bizinfo_rss.json', mode='rb') as f:
    detect_result = chardet.detect(f.read(50))
    if detect_result:
        encoding = detect_result['encoding']


# file read
with open('c:/Users/imcjp/workspace/vscode/python/json/bizinfo_rss.json', mode='rt', encoding=encoding) as f:
    rss_dict = json.load(f)

for item in rss_dict['jsonArray']:
    item_array = []
    for key in item.keys():
        # 내용 건너뛰기
        if(key == 'bsnsSumryCn'):
            continue

        item_array.append( str(item[key]) )
    
    print('|'.join( item_array ))