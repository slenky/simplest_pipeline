import argparse, json, shutil, os

def show_message(message:str):
    print("Message is: " + message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='parameter_parser')
    parser.add_argument('--message', type=str)
    args = parser.parse_args()
    
    # turn namespace into a dictionary
    argsIn = vars(args)
    
    show_message(**argsIn)
    
    print('Folder cleaned!')