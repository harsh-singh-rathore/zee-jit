import argparse
import os

from . import manage

def main ():
    args = parse_args ()
    args.monk(args)

def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command', title='for all the jit commands')
    commands.required = True
    
    init_parser = commands.add_parser('idhar')
    init_parser.set_defaults(monk = init)
    init_parser.add_argument('-p', '--path', help='Path to where you want to use jit bro')

    return parser.parse_args()
    

def init(args, path=os.getcwd()):
    if os.path.isdir(os.path.join(path, manage.JIT_DAR)):
        print("File already in jit man what you doing")
        return
    manage.init()
    print(f"Your directory for savign jit files was created at {path}/{manage.JIT_DAR}")
    
    
