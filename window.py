from tkinter import *
import random
import string
from cryptography.fernet import Fernet

class passwordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x200")
        self.generated_password = None
        self.encPassword = None
        self.key = Fernet.generate_key()

        self.fernet = Fernet(self.key)

        
        


        self.myButton = Button(self.root, text="Generate password", command=self.generatePassword)
        self.myTextfield = Entry(self.root, width=30)

        self.myTextfield.grid(row=0, column=0, padx=10, pady=20)
        self.myButton.grid(row=0, column=1, padx=10, pady=20)

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

        

       
        self.myTextfield.delete(0, END)
        self.myTextfield.insert(0, ''.join(password))
        self.generated_password = ''.join(password)

        

        self.encPassword = self.fernet.encrypt(self.generated_password.encode())

        print("Orginal String: ",self.generated_password)
        print("Encrypted string",self.encPassword)

if __name__ == "__main__":
    root = Tk()
    app = passwordManager(root)
    root.mainloop()
