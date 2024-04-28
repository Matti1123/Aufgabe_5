import my_functions as mf
import json
import my_classes as mc

# Experimentdaten
experiment_name = input("Geben sie Experimentname:")
Supervisor_fist_name = input("Geben sie Supervisor first_name:")
Supervisor_last_name = input("Geben sie Supervisor last_name:")
#supervisor_id = mc.Supervisor(Supervisor_fist_name,Supervisor_last_name, id)
supervisor_id = input("Geben sie supervisor_id ein:")
date = input("Geben date ein:")
subject = input("Geben subject ein:")

#Personendaten
first_name = input("Geben sie first_name:")
last_name = input("Geben sie last_name ein:")
sex = input("Geben sex ein:")
age = int(input("Geben age ein:"))
birthdate = input("Geben birthdate ein:")


if __name__ == "__main__":
    experiment = mc.Experiment(experiment_name,Supervisor_fist_name,supervisor_id,Supervisor_last_name,date,subject)
    print(experiment)
    mc.Experiment.save(experiment)

    subject = mc.Subject(first_name, last_name, sex, age,birthdate)
    mc.Subject.save(subject)
    print(subject)
    
    supervisor = mc.Supervisor(first_name, last_name)
    mc.Subject.save(subject)
    print(supervisor)

#with open("main.json", "a") as outfile: 
    #json.dump(experiment, outfile)


