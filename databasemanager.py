import json
import tkinter as tk
from tkinter import messagebox

def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

def add_person(database, person_id, name, age, nationality, sex, marital_status, sexuality, education_level, profession):
    if person_id not in database:
        database[person_id] = {
            'name': name,
            'age': age,
            'nationality': nationality,
            'sex': sex,
            'marital_status': marital_status,
            'sexuality': sexuality,
            'education_level': education_level,
            'profession': profession
        }
        message_text.set(f"Person with ID {person_id} added successfully.")
    else:
        message_text.set(f"Person with ID {person_id} already exists. Use update_person to modify.")

def check_person(database, person_id):
    if person_id in database:
        message_text.set(f"Person ID: {person_id}\n"
                         f"Name: {database[person_id]['name']}\n"
                         f"Age: {database[person_id]['age']}\n"
                         f"Nationality: {database[person_id]['nationality']}\n"
                         f"Sex: {database[person_id]['sex']}\n"
                         f"Marital Status: {database[person_id]['marital_status']}\n"
                         f"Sexuality: {database[person_id]['sexuality']}\n"
                         f"Education Level: {database[person_id]['education_level']}\n"
                         f"Profession: {database[person_id]['profession']}")
    else:
        message_text.set(f"Person with ID {person_id} not found.")

def update_person(database, person_id, name=None, age=None, nationality=None, sex=None, marital_status=None, sexuality=None, education_level=None, profession=None):
    if person_id in database:
        if name:
            database[person_id]['name'] = name
        if age:
            database[person_id]['age'] = age
        if nationality:
            database[person_id]['nationality'] = nationality
        if sex:
            database[person_id]['sex'] = sex
        if marital_status:
            database[person_id]['marital_status'] = marital_status
        if sexuality:
            database[person_id]['sexuality'] = sexuality
        if education_level:
            database[person_id]['education_level'] = education_level
        if profession:
            database[person_id]['profession'] = profession
        message_text.set(f"Person with ID {person_id} updated successfully.")
    else:
        message_text.set(f"Person with ID {person_id} not found.")

def add_person_gui():
    person_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    nationality = nationality_entry.get()
    sex = sex_entry.get()
    marital_status = marital_status_entry.get()
    sexuality = sexuality_entry.get()
    education_level = education_level_entry.get()
    profession = profession_entry.get()

    add_person(people_db, person_id, name, age, nationality, sex, marital_status, sexuality, education_level, profession)
    refresh_display()

def check_person_gui():
    person_id = id_entry.get()
    check_person(people_db, person_id)

def update_person_gui():
    person_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    nationality = nationality_entry.get()
    sex = sex_entry.get()
    marital_status = marital_status_entry.get()
    sexuality = sexuality_entry.get()
    education_level = education_level_entry.get()
    profession = profession_entry.get()

    update_person(people_db, person_id, name, age, nationality, sex, marital_status, sexuality, education_level, profession)
    refresh_display()

def save_and_exit():
    save_data(people_db, file_name)
    root.destroy()

def refresh_display():
    result_text.delete(1.0, tk.END)
    for person_id in people_db:
        result_text.insert(tk.END, f"Person ID: {person_id}\n")
        result_text.insert(tk.END, f"Name: {people_db[person_id]['name']}\n")
        result_text.insert(tk.END, f"Age: {people_db[person_id]['age']}\n")
        result_text.insert(tk.END, f"Nationality: {people_db[person_id]['nationality']}\n")
        result_text.insert(tk.END, f"Sex: {people_db[person_id]['sex']}\n")
        result_text.insert(tk.END, f"Marital Status: {people_db[person_id]['marital_status']}\n")
        result_text.insert(tk.END, f"Sexuality: {people_db[person_id]['sexuality']}\n")
        result_text.insert(tk.END, f"Education Level: {people_db[person_id]['education_level']}\n")
        result_text.insert(tk.END, f"Profession: {people_db[person_id]['profession']}\n\n")

# Main program
file_name = "people_database.json"
people_db = load_data(file_name)

root = tk.Tk()
root.title("People Database GUI")

# Entry fields
id_label = tk.Label(root, text="Person ID:")
id_entry = tk.Entry(root)

name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

age_label = tk.Label(root, text="Age:")
age_entry = tk.Entry(root)

nationality_label = tk.Label(root, text="Nationality:")
nationality_entry = tk.Entry(root)

sex_label = tk.Label(root, text="Sex:")
sex_entry = tk.Entry(root)

marital_status_label = tk.Label(root, text="Marital Status:")
marital_status_entry = tk.Entry(root)

sexuality_label = tk.Label(root, text="Sexuality:")
sexuality_entry = tk.Entry(root)

education_level_label = tk.Label(root, text="Education Level:")
education_level_entry = tk.Entry(root)

profession_label = tk.Label(root, text="Profession:")
profession_entry = tk.Entry(root)

# Buttons
add_button = tk.Button(root, text="Add Person", command=add_person_gui)
check_button = tk.Button(root, text="Check Person", command=check_person_gui)
update_button = tk.Button(root, text="Update Person", command=update_person_gui)
save_exit_button = tk.Button(root, text="Save and Exit", command=save_and_exit)

# Result display
result_text = tk.Text(root, height=15, width=50)

# Message display
message_text = tk.StringVar()
message_label = tk.Label(root, textvariable=message_text)

# Grid layout
id_label.grid(row=0, column=0, padx=10, pady=5)
id_entry.grid(row=0, column=1, padx=10, pady=5)

name_label.grid(row=1, column=0, padx=10, pady=5)
name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label.grid(row=2, column=0, padx=10, pady=5)
age_entry.grid(row=2, column=1, padx=10, pady=5)

nationality_label.grid(row=3, column=0, padx=10, pady=5)
nationality_entry.grid(row=3, column=1, padx=10, pady=5)

sex_label.grid(row=4, column=0, padx=10, pady=5)
sex_entry.grid(row=4, column=1, padx=10, pady=5)

marital_status_label.grid(row=5, column=0, padx=10, pady=5)
marital_status_entry.grid(row=5, column=1, padx=10, pady=5)

sexuality_label.grid(row=6, column=0, padx=10, pady=5)
sexuality_entry.grid(row=6, column=1, padx=10, pady=5)

education_level_label.grid(row=7, column=0, padx=10, pady=5)
education_level_entry.grid(row=7, column=1, padx=10, pady=5)

profession_label.grid(row=8, column=0, padx=10, pady=5)
profession_entry.grid(row=8, column=1, padx=10, pady=5)

add_button.grid(row=9, column=0, pady=10)
check_button.grid(row=9, column=1, pady=10)
update_button.grid(row=9, column=2, pady=10)

result_text.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

message_label.grid(row=11, column=0, columnspan=3, pady=10)

save_exit_button.grid(row=12, column=0, columnspan=3, pady=10)

# Start the GUI
root.mainloop()
