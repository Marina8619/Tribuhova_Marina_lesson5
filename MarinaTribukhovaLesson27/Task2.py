# Задание 2 (I). Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска
# XPATH. Попробуйте осуществить поиск содержимого по созданному документу XML, усложняя
# свои запросы и добавляя новые элементы, если потребуется.
import os
from xml.etree import ElementTree as ET
BASE_PATH = os.path.join(os.path.dirname(__file__))
PATH = BASE_PATH + '/data'
FILE_NAME_XML = '/output.xml'


root = ET.Element('studentslist')

for i in range(3):
    student = ET.SubElement(root, 'student', attrib={'id': str(i+1)})
    lastname = ET.SubElement(student, 'lastname')
    firstname = ET.SubElement(student, 'firstname')
    course = ET.SubElement(student, 'course')
    average_score = ET.SubElement(student, 'average_score')
    programming = ET.SubElement(average_score, 'programming')
    design = ET.SubElement(average_score, 'design')

root[0][0].text = 'Ivanov'
root[0][1].text = 'Ivan'
root[0][2].text = str(1)
root[0][3][0].text = str(10)
root[0][3][1].text = str(7)
root[1][0].text = 'Petrov'
root[1][1].text = 'Petr'
root[1][2].text = str(2)
root[1][3][0].text = str(9)
root[1][3][1].text = str(8)
root[2][0].text = 'Volkova'
root[2][1].text = 'Maria'
root[2][2].text = str(4)
root[2][3][0].text = str(8)
root[2][3][1].text = str(7)

#добавлю аттрибуты и значение
programming1 = root[0][3][0]
programming1.set('language', 'C++')
programming2 = root[1][3][0]
programming2.set('language', 'C#')
programming3 = root[2][3][0]
programming3.set('language', 'Python')
#увеличение среднего балла по дизайну у Волковой Марии
maria = root[2][3][1]
design3 = next(maria.iter('design'))
print(design3, design3.text)
design3.text = str(float(design3.text) + 1)
print(design3, design3.text)
#добавление нового предмета Ивану
ivan = root[0][3]
databases = ET.SubElement(ivan, 'databases')
databases.text = 'learning sql'
tree = ET.ElementTree(root)
tree.write(PATH + FILE_NAME_XML, encoding='utf-8')
#вывод элементов
ET.dump(tree)

#вывод всех студентов, используя XPATH, относительный путь
for elem in tree.findall('.//lastname'):
    print(elem.text)
stud2 = root.find(".//student[@id='2']")
print(stud2.tag, stud2.attrib)
for i in stud2:
    if i.tag == 'average_score':
        continue
    print(i.tag, i.text)
#вывод средних баллов по программированию, используя XPATH
for elem in tree.findall('student/average_score/programming'):
    print(elem.text)
#вывод средних баллов по дизайну, используя XPATH, относительный путь
for elem in tree.findall('.//design'):
    print(elem.text)






