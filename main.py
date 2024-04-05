import my_functions

experiment_name = input("Geben sie Experimentname:")
supervisor = input("Geben supervisor ein:")
date = input("Geben date ein:")
subject = input("Geben subject ein:")



if __name__ == "__main__":
    print(my_functions.build_experiment(experiment_name,supervisor,date,subject))

