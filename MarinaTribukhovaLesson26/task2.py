# Задание 2 (I). Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и
# попробуйте загрузить данные из файла
import json
data ={
  'books': {
        "Pushkin": "Captain's daughter",
        "Akunin": "Azazel",
        "Tolstoi": "War and peace"
    },
    'films': {
        "Gaidai": "Diamond hand",
        "Danelia": "Afonya",
        "Ryazanov": "Office romance"
    },
   'pets': {
        'cat': "Murka",
        'dog': "Oskar",
        "turtle": 'Tommi'
    }
}

json_data = json.dumps(data, indent=4)

#записываю в файл
with open('data/output_task2.json', 'w') as file_in:
    json.dump(data, file_in)
#загружаю из файла
with open('data/output_task2.json', 'r') as file_out:
    json_data_read = json.load(file_out)
    print(json_data_read)



