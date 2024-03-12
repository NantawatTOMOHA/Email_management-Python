#!/usr/bin/env python3
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
    if len(sys.argv) < 2 or (not sys.argv[1].startswith("--") and not sys.argv[1].startswith("-")) or len(sys.argv) > 3:
        print("Error: Invalid option or argument. Use --help for usage information.")
        sys.exit(1)

    command = sys.argv[1].lower()
    file_path = "/home/Email_management-Python/src/list_email.txt"
    

    if command == "--add" or command == "-a":
        if len(sys.argv[2]) > 76:
            print("Error: The email address is too long (maximum 76 characters).")
            sys.exit(1)
        
        if not sys.argv[2].endswith("@kmitl.ac.th"):
            print("Error: Invalid option or argument. Use --help for usage information.")
            sys.exit(1)

        if len(sys.argv) < 3:
            print("Error: Invalid option or argument. Use --help for usage information.")
            sys.exit(1)
        new_data = sys.argv[2]
        add_data(file_path, new_data)

    elif command == "--remove" or command == "-r":
        if len(sys.argv[2]) > 76:
            print("Error: The email address is too long (maximum 76 characters).")
            sys.exit(1)

        if len(sys.argv) < 3:
            print("Error: Invalid option or argument. Use --help for usage information.")
            sys.exit(1)
        target_data = sys.argv[2]
        remove_data(file_path, target_data)

    elif command == "--list" or command == "-li":
        if not len(sys.argv) == 2:
            print("Error: Invalid option or argument. Use --help for usage information.")
            sys.exit(1)
        list_data(file_path)

    elif command == "--help":
        print("Usage: analyze_email [OPTIONS]")
        print()
        print("analyze_email is a command line instruction using to manage email addresses in analysis.service")
        print()
        print("  Option              Long Option                                 Meaning")
        print("  -li                 --list                                      list all email addresses to service")
        print("  -a <email address>  --add <email address>                       add email address to service")
        print("  -r <email address>  --remove <email address>                    remove email address from service")
        print()
        print("Specify the email address with @kmitl.ac.th domain")
    else:
        print("Error: Invalid option or argument. Use --help for usage information.")
        sys.exit(1)

if __name__ == "__main__":
    main()
