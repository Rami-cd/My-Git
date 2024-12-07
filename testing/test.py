"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', type=str, help="your name", required=True)
parser.add_argument('--age', type=int, help="your age", default=18)

args = parser.parse_args()
print(f"Name: {args.name}, Age: {args.age}")
"""


def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def main():
    name = input("Enter your name: ")
    greet(name)
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()


import configparser

config = configparser.ConfigParser()
config.read('.gitconfig')

# Check if the 'user' section exists
if config.has_section('user'):
    user_name = config['user']['name']
    print(f"User Name: {user_name}")
else:
    print("Section 'user' not found in the config file.")

# Print all sections and keys in the config file
for section in config.sections():
    print(f"Section: {section}")
    for key, value in config.items(section):
        print(f"  {key} = {value}")    

# Accessing values
user_name = config['user']['name']
print(f"User Name: {user_name}")

# Adding sections and options
config.add_section('user')
config.set('user', 'name', 'John Doe')
config.set('user', 'email', 'john.doe@example.com')

# Write to a new file
with open('new_config.ini', 'w') as configfile:
    config.write(configfile)
    

import os
import pwd
import grp

# Simulate file metadata
file_stat = os.stat('example.txt')  # Replace with your file
uid = file_stat.st_uid
gid = file_stat.st_gid

# Resolve UID to username
user_name = pwd.getpwuid(uid).pw_name
# Resolve GID to group name
group_name = grp.getgrgid(gid).gr_name

print(f"File Owner: {user_name}, Group: {group_name}")

from fnmatch import fnmatch



import argparse

argparser = argparse.ArgumentParser(description="main program")

argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

command1_parser = argsubparsers.add_parser('command1', help="Excute command1")
command1_parser.add_argument('arg1', type=int, help="argument for command1")
command1_parser.add_argument('arg2', type=str, help="argument for command1")

args = argparser.parse_args()

if args.command == 'command1':
    print(f"Executing command1 with arguments: {args.arg1} {args.arg2}")
    

print(type('\x00'))