from tkinter import *
import random
import string
from cryptography.fernet import Fernet

class passwordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("1000x1000")
        self.generated_password = None
        self.encPassword = None
        self.decPassword = None
        self.key = Fernet.generate_key()

        self.fernet = Fernet(self.key)

        
        


        self.gp_button = Button(self.root, text="Generate password", command=self.generatePassword)
        self.sp_button = Button(self.root, text="Save password")
        self.password_testfield = Entry(self.root, width=30,fg = "grey")
        self.link_textfield = Entry(self.root,width = 30,fg = "grey")
        self.set_placeholder(self.link_textfield, "Please enter the link")
        self.set_placeholder(self.password_testfield, "Password")

        self.link_textfield.grid(row=0, column=0, padx=10, pady=20)
        self.password_testfield.grid(row=0, column=1, padx=10, pady=20)
        self.gp_button.grid(row=0, column=2, padx=10, pady=20)
        self.sp_button.grid(row = 0,column = 3,padx = 10,pady = 20)

    def set_placeholder(self, field, placeholder_text):
        field.insert(0,placeholder_text)

        def on_focus_in(event):
            if field.get() == placeholder_text:
                field.delete(0,END)
                field.config(fg = "white")
        def on_focus_out(event):
            if not field.get():
                field.insert(0,placeholder_text)
                field.config(fg = "grey")
        field.bind("<FocusIn>", on_focus_in)
        field.bind("<FocusOut>", on_focus_out)

    def generatePassword(self):
        lower = string.ascii_lowercase 
        upper = string.ascii_uppercase  
        digits = string.digits          
        special = string.punctuation   

        
        all_characters = lower + upper + digits + special
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special)
        ]

       
        length = 12  

        
        password += random.choices(all_characters, k=length - 4)

       
        random.shuffle(password)

        

       
        self.password_testfield.delete(0, END)
        self.password_testfield.insert(0, ''.join(password))
        self.generated_password = ''.join(password)

        

        self.encPassword = self.fernet.encrypt(self.generated_password.encode())
        self.decPassword  = self.fernet.decrypt(self.encPassword).decode()
        self.password_testfield.config(fg = "white")
        print("Orginal String: ",self.generated_password)
        print("Encrypted string",self.encPassword)
        print("Decrypted string",self.decPassword)



if __name__ == "__main__":
    root = Tk()
    app = passwordManager(root)
    root.mainloop()
