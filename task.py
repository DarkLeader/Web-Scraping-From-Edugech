from bs4 import BeautifulSoup
import requests
import csv

def get_urls():

    venu_list = []

    source = requests.get("https://edu.ge.ch/moodle/course/index.php?fbclid=IwAR2EcCIKG8Iho3r9V39Bf1L4zofZxvOYUy9Nsx4nALcriqye5C2iRAgnH5E")
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    sup = soup.find('div', class_ = 'subcategories')
    links = sup.find_all('a', href = True)
    for link in links:
        href = link.get('href')
        venu_list.append(href)
    return venu_list

def get_inside_urls():
    venu_list2 = []
    for i in get_urls():
        source3 = requests.get(i)
        soup = BeautifulSoup(source3.text, 'html.parser')
        soup3 = soup.find('div', class_='content')
        links3 = soup3.find_all('a', href=True)

        for alllinks in links3:
            href3 = alllinks.get('href')
            venu_list2.append(href3)
    return venu_list2

def teacher_names():
    mylist1 = []
    clearlist1 = []
    for x in get_urls():

        source2 = requests.get(x)
        soup2 = BeautifulSoup(source2.text, 'html.parser')
        try:
            sup2 = soup2.find_all('ul', class_='teachers')
            for x in sup2:
                sup45 = x.find_all('li')
                for z in sup45:
                    mylist1.append(z.text)
        except:
            pass
    for cleanings in mylist1:
        try:
            clearlist1.append(cleanings.replace("Teacher: ", ""))

        except:
            pass
    return clearlist1


def teacher_names_inside_links():
    mylist2 = []
    clearlist2 = []
    for z in get_inside_urls():

        try:
            source4 = requests.get(z)
            soup4 = BeautifulSoup(source4.text, 'html.parser')
            sup4 = soup4.find_all('ul', class_='teachers')
            for x in sup4:
                sup45 = x.find_all('li')
                for z in sup45:
                    mylist2.append(z.text)
        except:
            pass
    for cleanings2 in mylist2:
        try:
            clearlist2.append(cleanings2.replace("Teacher: ", ""))


        except:
            pass
    return clearlist2


result_list =  []
result_list2 = []
for x in teacher_names():
    data = {
        'teachers' : x

    }
    result_list.append(data)

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames=['teachers']
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result_list)

for z in teacher_names_inside_links():
    data2 = {
        'teachers' : z

    }
    result_list2.append(data2)

with open('names2.csv', 'w', newline='') as csvfile:
    fieldnames=['teachers']
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result_list2)









