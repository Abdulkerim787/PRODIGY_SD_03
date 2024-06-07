import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}

    def edit_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
        else:
            messagebox.showerror("Error", "Contact not found")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            messagebox.showerror("Error", "Contact not found")

    def save_contacts_to_file(self, filename):
        with open(filename, 'w') as f:
            for name, info in self.contacts.items():
                f.write(f"{name},{info['phone']},{info['email']}\n")

    def load_contacts_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, phone, email = line.strip().split(',')
                self.contacts[name] = {'phone': phone, 'email': email}

class ContactGUI:
    def __init__(self, root, contact_manager):
        self.root = root
        self.contact_manager = contact_manager

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1)

        tk.Label(self.root, text="Email:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=3, column=0)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=3, column=1)
        tk.Button(self.root, text="Edit Contact", command=self.edit_contact).grid(row=4, column=0)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=4, column=1)
        tk.Button(self.root, text="Save Contacts", command=self.save_contacts).grid(row=5, column=0)
        tk.Button(self.root, text="Load Contacts", command=self.load_contacts).grid(row=5, column=1)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()

        if name and phone and email:
            self.contact_manager.add_contact(name, phone, email)
            messagebox.showinfo("Success", "Contact added successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def view_contacts(self):
        contact_list = ""
        for name, info in self.contact_manager.contacts.items():
            contact_list += f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n"
        messagebox.showinfo("Contacts", contact_list)

    def edit_contact(self):
        name = simpledialog.askstring("Edit Contact", "Enter the name of the contact you want to edit:")
        if name:
            if name in self.contact_manager.contacts:
                phone = self.phone_var.get()
                email = self.email_var.get()
                self.contact_manager.edit_contact(name, phone, email)
                messagebox.showinfo("Success", "Contact edited successfully")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Contact not found")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact you want to delete:")
        if name:
            if name in self.contact_manager.contacts:
                self.contact_manager.delete_contact(name)
                messagebox.showinfo("Success", "Contact deleted successfully")
            else:
                messagebox.showerror("Error", "Contact not found")

    def save_contacts(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt")
        if filename:
            self.contact_manager.save_contacts_to_file(filename)
            messagebox.showinfo("Success", "Contacts saved successfully")

    def load_contacts(self):
        filename = tk.filedialog.askopenfilename()
        if filename:
            self.contact_manager.load_contacts_from_file(filename)
            messagebox.showinfo("Success", "Contacts loaded successfully")

    def clear_entries(self):
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Management System")
    contact_manager = ContactManagementSystem()
    ContactGUI(root, contact_manager)
    root.mainloop()
