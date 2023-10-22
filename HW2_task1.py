# Function to parse user input into command and arguments
def parse_input(user_input):
    cmd, *args = user_input.split()  # Split user input into command and arguments
    cmd = cmd.strip().lower()  # Strip leading/trailing spaces and convert to lowercase
    return cmd, args  # Return the command and arguments as a tuple

# Decorator for input error handling
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter a valid command."

    return inner

# Function to add a contact to the contacts dictionary
@input_error
def add_contact(args, contacts):
    if len(args) == 2:  # Check if there are two arguments (name and phone)
        name, phone = args
        contacts[name] = phone  # Add the contact to the dictionary
        return "Contact added."
    else:
        return "Invalid command. Please provide name and phone number."

# Function to change the phone number of an existing contact
@input_error
def change_contact(args, contacts):
    if len(args) == 2:  # Check if there are two arguments (name and new phone)
        name, phone = args
        name = name.lower()  # Convert the input name to lowercase
        matching_names = [key for key in contacts if key.lower() == name] # Making it case-insensitive

        if matching_names:
            matched_name = matching_names[0]
            contacts[matched_name] = phone  # Update the phone number for the existing contact
            return f"Phone number updated for {matched_name}."
        else:
            return f"Contact {args[0]} not found."
    else:
        return "Invalid command. Please provide name and new phone number."

# Function to retrieve the phone number of a contact
@input_error
def get_phone(args, contacts):
    if len(args) == 1:  # Check if there is a single argument (contact name)
        name = args[0].lower()  # Convert the input name to lowercase
        matching_names = [key for key in contacts if key.lower() == name] # Making it case-insensitive

        if matching_names:
            matched_name = matching_names[0]
            return f"Phone number for {matched_name}: {contacts[matched_name]}"  # Retrieve and return the phone number
        else:
            return f"Contact {args[0]} not found."
    else:
        return "Invalid command. Please provide a single name."

# Function to list all contacts and their phone numbers
@input_error
def list_all(contacts):
    if len(contacts) > 0:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])  # Create a formatted string to show the list of users
        return result
    else:
        return "No contacts found."

# Main function to control the bot's interaction with the user
def main():
    contacts = {}  # Initialize an empty dictionary for storing contacts
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")  # Prompt the user for a command
        command, args = parse_input(user_input)  # Parse the user input into command and arguments

        if command in ["close", "exit"]:
            print("Good bye!")  # Exit the loop and print a bye-bye message
            break
        elif command == "hello":
            print("How can I help you?")  # Respond to a "hello" command
        elif command == "add":
            print(add_contact(args, contacts))  # Call the add_contact function
        elif command == "change":
            print(change_contact(args, contacts))  # Call the change_contact function
        elif command == "phone":
            print(get_phone(args, contacts))  # Call the get_phone function
        elif command == "all":
            print(list_all(contacts))  # Call the list_all function
        else:
            print("Invalid command.")  # Handle invalid commands

if __name__ == "__main__":
    main()  # Start the bot by calling the main function
