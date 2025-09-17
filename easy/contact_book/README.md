# Contact Book Application

A simple command-line contact book application built in Python that allows you to manage your contacts efficiently.

## Features

- **Add Contacts**: Store contact information including name, phone number, email, and address
- **View Contacts**: Display all contacts in a formatted list
- **Edit Contacts**: Update existing contact information (phone, email, or address)
- **Delete Contacts**: Remove contacts from the contact book
- **Interactive Menu**: User-friendly command-line interface

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional installation steps required

## Usage

### Running the Application

```bash
python src/contact_book.py
```

### Menu Options

When you run the application, you'll see the following menu:

```
--- Contact Book Application ---
1. Add contact
2. Edit contact
3. View contacts
4. Delete contact
5. Quit
```

### Adding a Contact

1. Select option `1` from the menu
2. Enter the contact's name, phone number, email, and address when prompted
3. The contact will be added to your contact book

### Viewing Contacts

1. Select option `3` from the menu
2. All contacts will be displayed with their complete information

### Editing a Contact

1. Select option `2` from the menu
2. Enter the name of the contact you want to edit
3. For each field (phone, email, address), either enter new information or press Enter to keep the current value
4. The contact will be updated with your changes

### Deleting a Contact

1. Select option `4` from the menu
2. Enter the name of the contact you want to delete
3. The contact will be removed from your contact book

## Code Structure

The application consists of a single `ContactBook` class with the following methods:

- `__init__()`: Initializes an empty contact book
- `add_contact(name, phone, email, address)`: Adds a new contact
- `view_contacts()`: Displays all contacts
- `edit_contact(name, phone, email, address)`: Updates contact information
- `delete_contact(name)`: Removes a contact

## Example Usage

```
--- Contact Book Application ---
1. Add contact
2. Edit contact
3. View contacts
4. Delete contact
5. Quit

Please choose an option: 1

Enter Contact name: John Doe
Enter Contact phone: +1-555-123-4567
Enter Contact email: john.doe@email.com
Enter Contact address: 123 Main St, City, State
Contact added successfully!
```