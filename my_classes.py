import json

class Person:
    def __init__(self, first_name,last_name,sex,age):
        self.name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
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
    
    def save(self):
        with open("person.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
class Experiment:
    def __init__(self,experiment_name,supervisor,date,subject):
        self.experiment_name = experiment_name
        self.supervisor = supervisor
        self.date = date
        self.subject = subject
    def save(self):
        with open("experiment.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
Person1 = Person(1,2,"male",4)
print(Person1.estimate_max_hr)
Person1.save()