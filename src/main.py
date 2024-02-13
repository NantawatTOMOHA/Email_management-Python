#!/usr/bin/env python3
# analyze_email --add <address>@gmail.com
import sys

def add_data(file_path, new_data):
    with open(file_path, 'r') as file:
        existing_data = file.readlines()

    # Check if new_data is already in the list
    if new_data + '\n' not in existing_data:
        with open(file_path, 'a') as file:
            file.write(new_data + '\n')
            print(f"Added '{new_data}' ")
    else:
        print(f"Data '{new_data}' already exists ")

def remove_data(file_path, target_data):
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if target_data is in the list
    if target_data + '\n' in lines:
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() != target_data:
                    file.write(line)
            print(f"Removed '{target_data}' ")
    else:
        print(f"Data '{target_data}' not found ")

def list_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        for line in data:
            print(line.strip())

def main():
    if len(sys.argv) < 2 or not sys.argv[1].startswith("--"):
        print("Usage:--add|--remove|--list [new_data]")
        sys.exit(1)

    command = sys.argv[1].lower()
    file_path = "/home/Email_management-Python/cache/list_email.txt"

    if command == "--add":
        if len(sys.argv) < 2:
            print("Usage:--add [new_data]")
            sys.exit(1)
        new_data = sys.argv[2]
        add_data(file_path, new_data)

    elif command == "--remove":
        if len(sys.argv) < 2:
            print("Usage:--remove [target_data]")
            sys.exit(1)
        target_data = sys.argv[2]
        remove_data(file_path, target_data)

    elif command == "--list":
        list_data(file_path)

    else:
        print("Invalid command. Use --add, --remove, or --list.")
        sys.exit(1)

if __name__ == "__main__":
    main()

