import json
from deep_translator import GoogleTranslator

def AutoTranslate(input_file, output_file, lang):
    translator = GoogleTranslator(source='auto', target=lang)

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f'data loaded from ${input_file}')
    
    tdata = {}
    for key, value in data.items():
        val = translator.translate(value)
        tdata[key] = val
    print(f'data translated to ${lang}')

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tdata, f, ensure_ascii=False, indent=4)
    print(f'data saved to ${output_file}')


input_file = 'en.json'
output_file_hi = 'hi.json'
# output_file_te = 'te.json'
# output_file_mr = 'mr.json'

AutoTranslate(input_file, output_file_hi, 'hi')
