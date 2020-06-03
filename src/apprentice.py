import json
from functools import reduce
import requests
import os

url = "https://api.wanikani.com/v2/assignments"
payload = {'srs_stages': '1,2,3,4'}
token = os.environ['WK_TOKEN']
headers = {'Authorization': f'Bearer {token}'}
r = requests.get(url, headers=headers, params=payload)

with open('./apprentice.json', 'w', encoding='utf-8') as f:
    f.write(r.text)
