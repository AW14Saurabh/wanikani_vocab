import json
from functools import reduce
import requests
import os

url = "https://api.wanikani.com/v2/assignments"
payload = {'subject_types': 'vocabulary'}
token = os.environ['WK_TOKEN']
headers = {'Authorization': f'Bearer {token}'}
r = requests.get(url, headers=headers, params=payload)

with open('./output/vocab_stats.json', 'w', encoding='utf-8') as f:
    f.write(r.text)
collection = r.json()

data = collection['data']
ids = list(map(lambda x: x['data']['subject_id'], data))
id_string = reduce(lambda x, y: str(x)+','+str(y), ids)

url = 'https://api.wanikani.com/v2/subjects'
payload = {'ids': id_string}
token = os.environ['WK_TOKEN']
headers = {'Authorization': f'Bearer {token}'}
r = requests.get(url, headers=headers, params=payload)

with open('./output/vocab.json', 'w', encoding='utf-8') as f:
    f.write(r.text)
