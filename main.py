import my_functions as mf
import json
import my_classes as mc

# Experimentdaten
experiment_name = input("Geben sie Experimentname:")
supervisor = input("Geben supervisor ein:")
date = input("Geben date ein:")
subject = input("Geben subject ein:")

#Personendaten
first_name = input("Geben sie first_name:")
last_name = input("Geben sie last_name ein:")
sex = input("Geben sex ein:")
age = int(input("Geben age ein:"))


if __name__ == "__main__":
    experiment = mc.Experiment(experiment_name,supervisor,date,subject)
    print(experiment)
    mc.Experiment.save(experiment)
    person = mc.Person(first_name, last_name, sex, age)
    mc.Person.save(person)
    print(person)
    

#with open("main.json", "a") as outfile: 
    #json.dump(experiment, outfile)


