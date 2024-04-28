import my_functions as mf
import json
import my_classes as mc
import numpy as np




if __name__ == "__main__":
    # Experimentdaten
    experiment_input = input("Geben sie Experimentname:")
    date = input("Geben date ein:")


    #Personendaten subject
    first_name = input("Geben sie first_name:")
    last_name = input("Geben sie last_name ein:")
    sex = input("Geben sex ein:")
    age = int(input("Geben age ein:"))
    birthdate = input("Geben birthdate ein:")

    #Personendaten supervisor
    supervisor_fist_name = input("Geben sie Supervisor first_name:")
    supervisor_last_name = input("Geben sie Supervisor last_name:")
    supervisor_id = input("Geben sie supervisor_id ein:")


    subject = mc.Subject(first_name, last_name, sex, age,birthdate)
    mc.Subject.save(subject)
    print(subject)
    
    supervisor = mc.Supervisor(supervisor_fist_name, supervisor_last_name, supervisor_id)
    mc.Supervisor.save(supervisor)
    print(supervisor)

    experiment = mc.Experiment(experiment_name = experiment_input,date = date ,subject = subject ,supervisor=supervisor)
    print(experiment)
    mc.Experiment.save(experiment)

#with open("main.json", "a") as outfile: 
    #json.dump(experiment, outfile)
