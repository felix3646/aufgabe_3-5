import json
from datetime import datetime

class Person:
    
    @staticmethod
    def load_person_data():
        """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names
    
    @staticmethod
    def find_person_data_by_name(suchstring):
        """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        #print(suchstring)
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            
            if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):

                return eintrag
        else:
            return {}
        
    @staticmethod
    def load_by_id(ID):
        '''A function that loads a person by id and returns the person as a dictionary.'''
        person_data = Person.load_person_data()

        if ID == "None":
            return None

        for eintrag in person_data:
            if eintrag["id"] == ID:
                return eintrag
        else:
            return {}
        
    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]
        #zusatz
        self.age = self.calc_age()
        self.max_heart_rate = self.calc_max_heart_rate()
        self.ekg_data = person_dict["ekg_tests"]
        self.ekg_data_path = person_dict["ekg_tests"][0]["result_link"]
        self.ekg_data_date = person_dict["ekg_tests"][0]["date"]
       


    def calc_age(self):
        '''A function that calculates the age of a person based on the date of birth.'''

        today = datetime.today()
        age = today.year - self.date_of_birth

        return age


    def calc_max_heart_rate(self):
        '''A function that calculates the maximum heart rate of a person.'''

        age = self.calc_age()
        max_heart_rate = 220 - age

        return max_heart_rate
    
    @staticmethod
    def get_person_by_id(ID):
        '''A function that returns a person object by id.'''
        person_dict = Person.load_by_id(ID)
        if person_dict == {}:
            print("Person not found")
            return None
        return Person(person_dict)


if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    person1 = Person(Person.find_person_data_by_name("Huber, Julian"))
    print(person1.calc_max_heart_rate())
    print(Person.load_by_id(1))
    print(Person.get_person_by_id(1))
    print(person1.ekg_data_date)
    print(person1.ekg_data_path)
    