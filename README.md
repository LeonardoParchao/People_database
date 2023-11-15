# People Database GUI

This Python script provides a simple graphical user interface (GUI) for managing a people database. Users can add, check, and update information about individuals in the database.

## Features

- **Add Person**: Add a new person to the database with various attributes such as name, age, nationality, sex, marital status, sexuality, education level, and profession.

- **Check Person**: Retrieve and display information about a specific person in the database using their unique identifier (ID).

- **Update Person**: Modify the information of an existing person in the database.

- **Save and Exit**: Save the current state of the database to a JSON file and close the application.

## Usage

1. Run the script, and the GUI window will appear.
2. Enter the person's details in the corresponding entry fields.
3. Use the buttons to perform actions like adding, checking, or updating a person.
4. The result display area will show information about the people in the database.
5. Messages at the bottom will provide feedback on the success or failure of operations.
6. Click "Save and Exit" to save changes and close the application.

## File Handling

The script utilizes a JSON file (`people_database.json`) to store the database. If the file doesn't exist, it will be created. The data is loaded at the start of the program and saved upon clicking "Save and Exit."

## Functions

- `load_data(file_name)`: Load data from a JSON file or return an empty dictionary if the file is not found.
- `save_data(data, file_name)`: Save the data to a JSON file.
- `add_person(...)`: Add a new person to the database.
- `check_person(...)`: Display information about a specific person.
- `update_person(...)`: Update the information of an existing person.

## GUI Components

- Entry fields for person attributes (ID, Name, Age, etc.).
- Buttons to trigger actions (Add Person, Check Person, Update Person, Save and Exit).
- Result display area to show information about people in the database.
- Message area to provide feedback on operations.

## Dependencies

- `json`: for reading and writing JSON files.
- `tkinter`: for creating the GUI.

## Notes

- Ensure that you have Python installed on your system to run this script.

Feel free to customize and extend the functionality based on your specific needs!
