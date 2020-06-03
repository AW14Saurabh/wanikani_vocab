import json

with open('./output/vocab_stats.json', encoding='utf-8') as f:
    collection = json.load(f)

assgn_data = collection['data']
id_srs = {}
for elem in assgn_data:
    iden = elem['data']['subject_id']
    id_srs[iden] = elem['data']['srs_stage']

with open('./output/vocab.json', encoding='utf-8') as f:
    collection = json.load(f)

assgn_data = collection['data']
id_char = {}
for elem in assgn_data:
    id_char[elem['id']] = elem['data']['characters']

combine = []
for key in id_srs:
    combine.append({'Vocab':id_char[key],'Stage':id_srs[key]})

with open('./output/stats.json', 'w', encoding='utf-8') as f:
    json.dump(combine, f, ensure_ascii=False)