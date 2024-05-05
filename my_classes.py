import json
import requests

class Person:
    def __init__(self, first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name
    
    def save(self):
        with open("person.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
            
    def put(self,url:str):
        # Defines the data putted to the API
        data = {
            "name": self.first_name
        }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)

        return(response.status_code)

class Subject(Person):
    def __init__(self,first_name:str,last_name:str,sex:str,age:int,birthdate:int,email:str):
        super().__init__(first_name,last_name)
        self.sex = sex
        self.age = age
        self.__birthdate = birthdate
        self.max_hr = self.estimate_max_hr(self.sex,self.age)
        self.email = email

    def update_email(self, url):
        # Defines the data posted to the API
        data = {
            "name": self.first_name,
            "email": self.email
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)

        return(response.status_code)

    '''def calculate_age(self,birthdate:int):
        age = 2024 - birthdate
        return age'''
        

    def estimate_max_hr(self,sex,age):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return max_hr_bpm



class Supervisor(Person):
    def __init__(self,first_name:str,last_name:str,supervisor_id:int):
        super().__init__(first_name = first_name,last_name = last_name)
        self.id = supervisor_id
        


class Experiment:
    def __init__(self,experiment_name:str,date:str,subject:Subject, supervisor:Supervisor):
        self.experiment_name = experiment_name
        self.date = date 
        self.supervisor_data = {
            "first_name" : supervisor.first_name,
            "last_name" : supervisor.last_name,
            "supervisor_id" : supervisor.id,
        }
        self.subject_data = {
            "first_name" : subject.first_name,
            "last_name" : subject.last_name,
        }

    def save(self):
        with open("experiment.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)

            
"""Person1 = Subject("Max","Must","male",25,1966)
print(Person1.estimate_max_hr)
Person1.save()

s1 = Supervisor("Domi","Dulli",3)
print(s1.__dict__)"""