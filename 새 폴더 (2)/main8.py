from xml.etree.ElementTree import *

person = Element('Person')

name = Element('name')
name.text = '홍길동'
person.append(name)

age = Element('age')
age.text = '15'
person.append(age)

SubElement(person, 'age').text = '16'  # 위에 3줄을 1줄로 줄일 수 있다

SubElement(person, 'address').text = '대구'

no=Element('no')
no.text = '17'
person.insert(1, no)

person.remove(no)

person.attrib['data'] = '2020-02-12'  # 속성
dump(person)

ElementTree(person).write('c:/Users/gotsl/Desktop/새 폴더 (2)/person.xml')