import json

class Person:
    def __init__(self, first_name,last_name):
        self.name = first_name
        self.last_name = last_name

    '''def estimate_max_hr(self,sex,age):
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return max_hr_bpm'''
    
    def save(self):
        with open("person.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)


class Subject(Person):
    def __init__(self,first_name,last_name,sex,age,birthdate):
        super().__init__(first_name,last_name)
        self.sex = sex
        self.age = age
        self.__birthdate = birthdate
        self.max_hr = self.estimate_max_hr(self.sex,self.age)

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
    def __init__(self,first_name,last_name,supervisor_id):
        super().__init__(first_name,last_name)
        self.id = supervisor_id
        


class Experiment:
    def __init__(self,experiment_name,Supervisor_fist_name,Supervisor_last_name,date,subject):
        self.experiment_name = experiment_name
        self.Supervisor_fist_name = Supervisor_fist_name
        self.Supervisor_last_name = Supervisor_last_name
        self.date = date
        self.subject = subject

    def save(self):
        with open("experiment.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)

            
"""Person1 = Subject("Max","Must","male",25,1966)
print(Person1.estimate_max_hr)
Person1.save()

s1 = Supervisor("Domi","Dulli",3)
print(s1.__dict__)"""