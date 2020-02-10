from random import randint, choice
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DataGen:
    def __init__(self):
        self.first_names = []
        self.surnames = []
        self.items = []
        self.roads = []
        self.towns = []
        self.sub_locations = []
        with open(os.path.join(BASE_DIR, 'core/static/core/first_names.txt'),'r') as f:
            for line in f:
                self.first_names.append(line.strip('\n'))
        with open(os.path.join(BASE_DIR, 'core/static/core/surnames.txt'),'r') as f:
            for line in f:
                self.surnames.append(line.strip('\n'))
        with open(os.path.join(BASE_DIR, 'core/static/core/roads.txt'),'r') as f:
            for line in f:
                self.roads.append(line.strip('\n'))
        with open(os.path.join(BASE_DIR, 'core/static/core/items.txt'),'r') as f:
            for line in f:
                self.items.append(line.strip('\n'))
        with open(os.path.join(BASE_DIR, 'core/static/core/towns.txt'),'r') as f:
            for line in f:
                self.towns.append(line.strip('\n'))
        with open(os.path.join(BASE_DIR, 'core/static/core/sub_locations.txt'),'r') as f:
            for line in f:
                self.sub_locations.append(line.strip('\n'))

    def date_of_birth(self):
        day = str(randint(1,30))
        month = str(randint(1,12))
        year = str(randint(1930,2010))
        return day+'/'+month+'/'+year

    def group_id(self):
        return '97/'+str(randint(0,9000))+'/19'

    def seized_by(self):
        return str(randint(0,335))

    def seized_time(self):
        return str(randint(1,23))+':'+str(randint(0,59))

    def seized_date(self):
        return '2019-'+str(randint(1,12))+'-'+str(randint(1,28))

    def exhibit_ref(self):
        return str(randint(1,335))+'/'+str(randint(1,50))

    def road(self):
        return self.roads[randint(0,len(self.roads)-1)]

    def town(self):
        return self.towns[randint(0,len(self.towns)-1)]

    def first_name(self):
        return self.first_names[randint(0,len(self.first_names)-1)]

    def surname(self):
        return self.surnames[randint(0,len(self.surnames)-1)]

    def sub_location(self):
        return self.sub_locations[randint(0,len(self.sub_locations)-1)]

    def item(self):
        item_list = self.items[randint(0,len(self.items)-1)]
        return item_list

    def postcode(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return 'IM'+str(randint(1,9))+' '+choice(letters)+choice(letters)+choice(letters)

    def house_number(self):
        return str(randint(1,60))

    def sealnumber(self):
        return 'N'+str(randint(0,999999))
