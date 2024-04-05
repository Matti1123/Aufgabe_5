import my_functions
import json

experiment_name = input("Geben sie Experimentname:")
supervisor = input("Geben supervisor ein:")
date = input("Geben date ein:")
subject = input("Geben subject ein:")



if __name__ == "__main__":
    experiment = my_functions.build_experiment(experiment_name,supervisor,date,subject)
    print(experiment)


with open("sample.json", "a") as outfile: 
    json.dump(experiment, outfile)


