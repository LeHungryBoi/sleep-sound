import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("-f", "--force", help="force boom outside working hour", 
action="store_true")



def ParseArguments():
    args = parser.parse_args()