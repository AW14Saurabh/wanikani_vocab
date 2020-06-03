import json

with open('./guru_1.json', encoding='utf-8') as f:
    collection = json.load(f)

assgn_data = collection['data']
kanji = 0
vocab = 0
radical = 0
kanji_avl_at = []
vocab_avl_at = []
radic_avl_at = []
for assgn in assgn_data:
    subject = assgn['data']['subject_type']
    if subject == 'kanji':
        kanji += 1
        kanji_avl_at.append(assgn['data']['available_at'])
    elif subject == 'vocabulary':
        vocab += 1
        vocab_avl_at.append(assgn['data']['available_at'])
    elif subject == 'radical':
        radical += 1
        radic_avl_at.append(assgn['data']['available_at'])
print(f'Kanji: {kanji}\nVocabulary: {vocab}\nRadical: {radical}\n')
print('Kanji:')
print(*kanji_avl_at, sep='\n')
print('Vocabulary:')
print(*vocab_avl_at, sep='\n')
print('Radical:')
print(*radic_avl_at, sep='\n')
