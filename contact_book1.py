import tkinter as tk
from tkinter import messagebox

contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name}: {info['phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['phone']:
            contact_list.insert(tk.END, f"{name}: {info['phone']}")

# Function to update a contact
def update_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0]
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Select a contact to update")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0]
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Select a contact to delete")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Setting up the main application window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x400")

# Labels and Entry fields for contact details
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry.grid(row=2, column=1, padx=10, pady=5)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons for contact operations
add_button = tk.Button(root, text="Add Contact", command=add_contact)
update_button = tk.Button(root, text="Update Contact", command=update_contact)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)

add_button.grid(row=4, column=0, columnspan=2, pady=10)
update_button.grid(row=5, column=0, columnspan=2, pady=10)
delete_button.grid(row=6, column=0, columnspan=2, pady=10)

# Search bar and button
tk.Label(root, text="Search").grid(row=7, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=7, column=1, padx=10, pady=5)
search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=7, column=2, padx=10, pady=5)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# Populate the listbox with contacts
view_contacts()

# Run the application
root.mainloop()
