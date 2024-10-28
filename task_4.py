def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as name:
            return f"There is no contact with a name {name}"
        except IndexError:
            return "Error: Missing required arguments."

    return inner
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Both name and phone are required.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Both name and phone are required.")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError(name)
    
@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError("No name provided.")
    name = args[0]
    if name in contacts:
        return f"{contacts[name]} {name}"
    else:
        raise KeyError(name)
    
def all_contact():
    return contacts


def main():
    global contacts 
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all_contact())

        else:
            print(command, args)
            print("Invalid command.")

if __name__ == "__main__":
    main()