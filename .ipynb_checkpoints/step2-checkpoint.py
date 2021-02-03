import argparse, json, shutil, os

def count_scenarios(scenarios:int):
    print("Scenarios count: " + scenarios)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='parameter_parser')
    parser.add_argument('--scenarios', type=int)
    args = parser.parse_args()
    
    # turn namespace into a dictionary
    argsIn = vars(args)
    
    count_scenarios(**argsIn)
    
    print('Folder cleaned!')